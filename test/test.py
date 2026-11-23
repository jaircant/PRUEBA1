# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    # A = 1101 (13), B = 0010 (2)
    # A3 y B3 entran por uio_in[0] y uio_in[1].
    dut.uio_in.value = 0b01

    # ui_in, en orden: ENABLE, SELECTOR, B[2:0], A[2:0]
    for entrada, esperado in [
        (0b1_0_010_101, 13),  # Habilitado, selecciona A
        (0b1_1_010_101,  2),  # Habilitado, selecciona B
        (0b0_0_010_101,  0),  # Deshabilitado con selector 0
        (0b0_1_010_101,  0),  # Deshabilitado con selector 1
    ]:
        dut.ui_in.value = entrada
        await ClockCycles(dut.clk, 1)
        assert int(dut.uo_out.value) == esperado

    # Comprueba también que B3 llega a la salida.
    dut.uio_in.value = 0b10
    dut.ui_in.value = 0b1_1_010_101
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == 10
    # one or more clock cycles, and asserting the expected output values.
