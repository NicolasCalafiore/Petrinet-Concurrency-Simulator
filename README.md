# Petrinet-Concurrency-Simulator

A Python simulator that models pipeline coordination and simulated concurrency in sequential execution flow using Petri-net-inspired places and transitions.

## Project Overview

This project explores how concurrent behavior can be represented without multithreading by coordinating independent pipeline stages across discrete clock cycles. Instructions, register values, and data-memory values move through stage buffers as tokens, while transition rules control when each stage can execute.

## Technical Highlights

- Built a place/transition simulation architecture to represent pipeline stages and data movement
- Modeled single-thread concurrency through cycle-based stage coordination
- Implemented tick-based token gating (`arrival_tick`) to enforce execution ordering and stage readiness
- Added instruction decode/read behavior that resolves register operands before issue
- Split issue paths into arithmetic and load-style flows to simulate parallel pipeline tracks
- Centralized transition logic (`DECODE`, `ISSUE`, `ALU`, `ADDR`, `LOAD`, `WRITE`) for clear execution flow
- Added debug logging to trace stage executability, token transfers, and cycle progression
- Drove simulation state from external input files for instructions, registers, and data memory

## Pipeline Model

### Places

- `INM`: instruction memory queue
- `INB`: decoded instruction buffer
- `AIB`: arithmetic instruction buffer
- `LIB`: load instruction buffer
- `ADB`: address buffer
- `REB`: result buffer
- `RGF`: register file
- `DAM`: data memory

### Transitions

- `DECODE`: moves instruction from `INM` to `INB` and resolves source register values
- `ISSUE1`: routes arithmetic/logic instructions from `INB` to `AIB`
- `ISSUE2`: routes load-style instructions from `INB` to `LIB`
- `ALU`: executes arithmetic flow from `AIB` toward `REB`
- `ADDR`: advances load path from `LIB` to `ADB`
- `LOAD`: transfers memory/load-related results into `REB`
- `WRITE`: commits buffered results from `REB` into `RGF`

## Input-Driven Simulation

The simulator consumes three text inputs:

- `instructions.txt`: instruction stream tokens
- `registers.txt`: initial register state
- `datamemory.txt`: initial data-memory state

Each cycle evaluates stage readiness and applies transitions in order to advance tokens through the pipeline.

## Core Files

- `script.py`: simulation driver, cycle loop, input loading, and component printing
- `places.py`: place abstractions, token model, stage storage, and executability checks
- `transitions.py`: transition functions defining inter-stage movement and stage actions
- `instructions.txt`, `registers.txt`, `datamemory.txt`: scenario inputs for simulation state

## Lessons Learned

- **Single-thread concurrency modeling:** representing concurrent behavior through coordinated stage progression instead of parallel threads
- **Pipeline state machines:** designing stage-specific readiness checks to control token flow safely across cycles
- **Synchronization by timing:** using arrival-tick constraints to avoid invalid same-cycle consumption and preserve deterministic order
- **Instruction/data decoupling:** separating decode, execute, address, load, and write-back concerns into explicit transition steps
