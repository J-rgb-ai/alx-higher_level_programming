#!/usr/bin/python3
"""Deffines an object attribute lookupfunction."""

def lookup(obj):
    """Returns the list of an object's available attributes."""
    return (dir(obj))
