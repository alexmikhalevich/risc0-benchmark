PAYLOAD ?= sort
VERIFY_STEP_LENGTH_CYCLES ?= 1000
VERIFY_LOG_PATH ?= $(CURDIR)/log.bin
CARTESI_ROOTFS_PATH ?= rootfs.ext2

MACHINE_LOG = .machine.log
PROVER_LOG = deps/prover/.prover.log
PROVER_ENV = deps/prover/.env

all:
	@rm -f $(PROVER_ENV)
	@rm -f $(VERIFY_LOG_PATH)
	@rm -f $(MACHINE_LOG)
	$(MAKE) risc0-prove

visual:
	@python3 plot.py $(PAYLOAD)

payload:
	@make -C payload

cartesi-count-cycles:
	@cartesi-machine \
		--flash-drive=label:root,filename:$(CARTESI_ROOTFS_PATH) \
		--flash-drive=label:payload,filename:payload/payload.ext2 \
		-- /mnt/payload/opt/payload/$(PAYLOAD) 2>$(MACHINE_LOG) 1>/dev/null
	@CARTESI_CYCLES=$$(grep "^Cycles: " $(MACHINE_LOG) | awk -F ': ' '{print $$2}'); echo "{\"cycles\": $$CARTESI_CYCLES}"

cartesi-log:
	@cartesi-machine \
		--flash-drive=label:root,filename:$(CARTESI_ROOTFS_PATH) \
		--flash-drive=label:payload,filename:payload/payload.ext2 \
		--max-mcycle=0 \
		--log-step=$(VERIFY_STEP_LENGTH_CYCLES),$(VERIFY_LOG_PATH) \
		-- /mnt/payload/opt/payload/$(PAYLOAD) > $(MACHINE_LOG) 2>&1
	@START_HASH=$$(grep "^0:" $(MACHINE_LOG) | awk -F ': ' '{print $$2}'); \
	END_HASH=$$(grep "^$(VERIFY_STEP_LENGTH_CYCLES):" $(MACHINE_LOG) | awk -F ': ' '{print $$2}'); \
	echo "VERIFY_START_HASH=$$START_HASH" > $(PROVER_ENV); \
	echo "VERIFY_END_HASH=$$END_HASH" >> $(PROVER_ENV)

risc0-prove: cartesi-log
	@echo "RISC0_DEV_MODE=true" >> $(PROVER_ENV)
	@echo "RUST_LOG=info" >> $(PROVER_ENV)
	@echo "VERIFY_STEPS=$(VERIFY_STEP_LENGTH_CYCLES)" >> $(PROVER_ENV)
	@echo "VERIFY_LOG_PATH=$(VERIFY_LOG_PATH)" >> $(PROVER_ENV)
	@echo "ZKARCH_PATH=$(ZKARCH_PATH)" >> $(PROVER_ENV)
	@cd deps/prover && dotenv cargo run --release 1> .prover.log 2> /dev/null
	@echo ""
	@echo "===== Benchmark: $(PAYLOAD); step: $(VERIFY_STEP_LENGTH_CYCLES) ====="
	@echo "{" > result.json
	@echo "  \"benchmark\": \"$(PAYLOAD)\"," >> result.json
	@echo "  \"step\": $(VERIFY_STEP_LENGTH_CYCLES)," >> result.json
	@echo "  \"execution_time\": \"$$(awk -F 'execution time: ' 'NF > 1 {print $$2}' $(PROVER_LOG))\"," >> result.json
	@echo "  \"number_of_segments\": $$(awk -F 'number of segments: ' 'NF > 1 {print $$2}' $(PROVER_LOG))," >> result.json
	@echo "  \"total_cycles\": $$(awk -F 'total cycles: ' 'NF > 1 {print $$2}' $(PROVER_LOG))," >> result.json
	@echo "  \"user_cycles\": $$(awk -F 'user cycles: ' 'NF > 1 {print $$2}' $(PROVER_LOG))" >> result.json
	@echo "}" >> result.json
	@cat result.json

list:
	@echo "Available benchmark payloads:"
	@echo "  - sort: quicksort implementation (100k numbers)"

clean:
	@make -C payload clean
	@cd deps/prover && cargo clean

.PHONY: visual cartesi-log risc0-prove list clean
