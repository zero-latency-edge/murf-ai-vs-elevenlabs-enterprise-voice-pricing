#!/usr/bin/env python3
"""Murf AI vs ElevenLabs Enterprise Voice Pricing Calculator 2026."""
import argparse

def calculate(hours=10):
    # Murf AI Pro: $79/mo (billed annually as $948/yr), includes 24 hours of voice generation per year (2 hrs/mo).
    # Overage requires upgrading to Enterprise.
    murf_monthly = 79.0
    murf_included_hours_month = 2.0

    # ElevenLabs Pro: $82.50/mo (billed annually as $990/yr), includes 500k chars (~8.3 hours/mo).
    eleven_monthly = 82.50
    eleven_included_hours_month = 8.33

    print("=" * 65)
    print("Murf AI vs ElevenLabs: Professional Voice Generation TCO")
    print("=" * 65)
    print(f"Target Voice Production:   {hours} hours / month")
    print(f"Murf AI Pro Plan:          ${murf_monthly:.2f}/mo (Includes {murf_included_hours_month} hrs/mo)")
    print(f"ElevenLabs Pro Plan:       ${eleven_monthly:.2f}/mo (Includes {eleven_included_hours_month:.1f} hrs/mo)")
    print(f"Hours Allowance Advantage: ElevenLabs provides 4.1x more audio hours/mo")
    print("=" * 65)
    return murf_monthly, eleven_monthly

if __name__ == "__main__":
    calculate()
