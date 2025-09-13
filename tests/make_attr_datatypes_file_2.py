#! /usr/bin/env python

""" Create a HDF5 file with all the supported attribute types (2)"""
import h5py
import numpy as np


with h5py.File('attr_datatypes_2.hdf5', 'w') as ds:
    dt = h5py.string_dtype("utf-8")
    unicode = "unicodé"
    ds.attrs["unicode"] = unicode
    ds.attrs["unicode_0dim"] = np.array(unicode, dtype=dt)
    ds.attrs["unicode_1dim"] = np.array([unicode], dtype=dt)
    ds.attrs["unicode_arrary"] = np.array([unicode, "foobár"], dtype=dt)
    ds.attrs["unicode_list"] = [unicode]
    ds.attrs["unicode_list_empty"] = []
    
    dt = h5py.string_dtype("ascii")
    # if dtype is ascii it's irrelevant if the data is provided as bytes or string
    ascii = "ascii"
    ds.attrs["ascii"] = ascii
    ds.attrs["ascii_0dim"] = np.array(ascii, dtype=dt)
    ds.attrs["ascii_1dim"] = np.array([ascii], dtype=dt)
    ds.attrs["ascii_array"] = np.array([ascii, "foobar"], dtype=dt)
    ds.attrs["ascii_list"] = [ascii]
    ds.attrs["ascii_empty"] = ""

    ascii = b"ascii"
    ds.attrs["bytes"] = ascii
    ds.attrs["bytes_0dim"] = np.array(ascii, dtype=dt)
    ds.attrs["bytes_1dim"] = np.array([ascii], dtype=dt)
    ds.attrs["bytes_array"] = np.array([ascii, b"foobar"], dtype=dt)
    ds.attrs["bytes_list"] = [ascii]
    ds.attrs["bytes_empty"] = b""

    dt = h5py.string_dtype("utf-8", 10)
    # unicode needs to be encoded properly for fixed size string type
    ds.attrs["unicode_fixed"] = np.array(unicode.encode("utf-8"), dtype=dt)
    ds.attrs["unicode_fixed_0dim"] = np.array(unicode.encode("utf-8"), dtype=dt)
    ds.attrs["unicode_fixed_1dim"] = np.array([unicode.encode("utf-8")], dtype=dt)
    ds.attrs["unicode_fixed_arrary"] = np.array(
        [unicode.encode("utf-8"), "foobár".encode()], dtype=dt
    )
    
    dt = h5py.string_dtype("ascii", 10)
    ascii = "ascii"
    ds.attrs["ascii_fixed"] = np.array(ascii, dtype=dt)
    ds.attrs["ascii_fixed_0dim"] = np.array(ascii, dtype=dt)
    ds.attrs["ascii_fixed_1dim"] = np.array([ascii], dtype=dt)
    ds.attrs["ascii_fixed_array"] = np.array([ascii, "foobar"], dtype=dt)
    
    ascii = b"ascii"
    ds.attrs["bytes_fixed"] = np.array(ascii, dtype=dt)
    ds.attrs["bytes_fixed_0dim"] = np.array(ascii, dtype=dt)
    ds.attrs["bytes_fixed_1dim"] = np.array([ascii], dtype=dt)
    ds.attrs["bytes_fixed_array"] = np.array([ascii, b"foobar"], dtype=dt)
    
    ds.attrs["int"] = 1
    ds.attrs["intlist"] = [1]
    ds.attrs["int_array"] = np.arange(10)
    ds.attrs["empty_list"] = []
    ds.attrs["empty_array"] = np.array([])
    
