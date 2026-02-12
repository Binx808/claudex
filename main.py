#!/usr/bin/env python3
"""Legacy entry point for claudex.

DEPRECATED: Use the pip-installable package instead:
    pip install -e .
    claudex --help

This wrapper exists for backwards compatibility.
"""

import sys

print("=" * 70)
print("DEPRECATION NOTICE")
print("=" * 70)
print()
print("The standalone main.py script is deprecated.")
print("Please use the pip-installable package instead:")
print()
print("  pip install -e .")
print("  claudex --help")
print()
print("Forwarding to new CLI...")
print("=" * 70)
print()

# Forward to new CLI
from claudex.cli import main

if __name__ == "__main__":
    main()
