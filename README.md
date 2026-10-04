# SIP-CALCULATOR-WITH-INFLATION
A beginner-friendly Python SIP calculator with editable return and inflation rates, future value, estimated gains, and inflation-adjusted value.

# SIP Calculator

A small Python program that estimates the future value of a monthly SIP and adjusts that estimate for inflation.

## Features

- Enter a monthly SIP amount and investment period.
- Use an expected yearly return of **12%** by default.
- Use expected yearly inflation of **7%** by default.
- Press Enter to keep either default, or type another percentage.
- See the total invested, estimated returns, estimated future value, and estimated value in today's money.

## Requirements

- Python 3
- No extra packages required

## Run it

Open a terminal in the folder containing `sip_calculator.py`, then run:

```bash
python sip_calculator.py
```

If your system uses the `python3` command, run:

```bash
python3 sip_calculator.py
```

## Example

```text
SIP Calculator
Press Enter to use the default return and inflation rates.

Monthly SIP amount (₹): 5000
Investment period in years: 10
Expected yearly return % [12]:
Expected yearly inflation % [7]:
```

The program then displays an estimate based on a ₹5,000 monthly SIP over 10 years, using the default return and inflation rates.

## How the estimate works

The calculator assumes a fixed return rate compounded monthly and that each monthly investment is made at the beginning of the month. It estimates today's-money value by reducing the projected future value using the chosen inflation rate over the full investment period.

Actual investment returns and inflation change over time, so the result is only an estimate and is not guaranteed.
