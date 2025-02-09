# Quantum Paradox

## Clue / Information

Breach a quantum-secured darknet exchange by exploiting vulnerabilities in:
- Quantum Handshake Protocol
- Temporal Authentication
- Quantum WASM Processor

Flag Format: `BITSCTF{...}
Challenge Details

Server URL: http://chals.bitskrieg.in:3009/
Endpoints:
- `POST /qchannel` - Initialize quantum channel
- `GET /entangle` - Generate authentication token
- `POST /qproc` - Process quantum WASM modules
- `GET /vault/{something}` - Restricted flag storage

"Quantum protocols often reuse known entropy seeds for initialization."
"Not all algorithms validate their cryptographic claims."
"Memory superposition collapses at fixed boundaries."

## Resolution

The WebAssembly (Wasm) script in [processor.wasm](./processor.wasm) defines a simple module that exports a function named `process` and a linear memory named `memory`. Let's break it down:

### 1. **Memory Definition**
```wasm
(memory (export "memory") 1)
```
- This line defines a linear memory with an initial size of 1 page (64 KiB) and exports it with the name `"memory"`.
- Linear memory in WebAssembly is a contiguous, byte-addressable array that can be used for storing data.

### 2. **Function Definition**
```wasm
(func $process (param $size i32)
  (local $buf i32)
```
- The function `$process` is defined with one parameter:
  - `$size`: An `i32` (32-bit integer) representing the number of bytes to copy.
- It also declares a local variable:
  - `$buf`: An `i32` that will be used as an offset in memory.

### 3. **Local Variable Initialization**
```wasm
(local.set $buf (i32.const 64))
```
- The local variable `$buf` is set to the constant value `64`. This means the function will use memory starting at offset 64 as the destination for the copy operation.

### 4. **Memory Copy Operation**
```wasm
(memory.copy
  (local.get $buf)
  (i32.const 0)
  (local.get $size)
)
```
- The `memory.copy` instruction copies a block of memory from one location to another.
- Here, it copies `$size` bytes:
  - From the source offset `0` (beginning of memory).
  - To the destination offset `$buf` (which is set to 64).
- This effectively copies the first `$size` bytes of memory to the location starting at offset 64.

### 5. **Exporting the Function**
```wasm
(export "process" (func $process))
```
- The function `$process` is exported with the name `"process"`, making it callable from outside the WebAssembly module (e.g., from JavaScript).

---

### **What Does This Script Do?**
- The script defines a WebAssembly module with a single exported function `process`.
- When `process` is called with a `size` argument, it copies `size` bytes from the beginning of the memory (offset 0) to a location starting at offset 64.
- The exported memory (`"memory"`) can be accessed and manipulated from outside the module.

---

### **Potential Use Cases**
1. **Memory Manipulation**: This script could be used to move data around in memory, which might be useful in low-level operations or when interfacing with external systems.
2. **Data Processing**: If the memory contains structured data, this function could be part of a larger pipeline for processing or transforming that data.
3. **Interoperability**: The exported memory and function allow JavaScript or other host environments to interact with the WebAssembly module, passing data back and forth.

---
