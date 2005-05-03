"""M2Crypto wrapper for OpenSSL ASN1 API.

Copyright (c) 1999-2004 Ng Pheng Siong. All rights reserved."""

RCS_id='$Id: ASN1.py,v 1.4 2004/04/09 16:16:07 ngps Exp $'

import BIO
import m2

MBSTRING_FLAG = 0x1000
MBSTRING_ASC  = MBSTRING_FLAG | 1
MBSTRING_BMP  = MBSTRING_FLAG | 2


class ASN1_Integer:
    def __init__(self, asn1int, _pyfree=0):
        self.asn1int = asn1int
        self._pyfree = _pyfree


class ASN1_BitString:
    def __init__(self, asn1bitstr, _pyfree=0):
        self.asn1bitstr = asn1bitstr
        self._pyfree = _pyfree

    def __str__(self):
        buf = BIO.MemoryBuffer()
        m2.asn1_bit_string_print( buf.bio_ptr(), self.asn1bitstr )
        return buf.read_all()

    def __del__(self):
        try:
            if self._pyfree:
                m2.asn1_bit_string_free(self.asn1bitstr)
        except AttributeError:
            pass

    def _ptr(self):
        return self.asn1bitstr


class ASN1_String:
    def __init__(self, asn1str, _pyfree=0):
        self.asn1str = asn1str
        self._pyfree = _pyfree

    def __str__(self):
        buf = BIO.MemoryBuffer()
        m2.asn1_string_print( buf.bio_ptr(), self.asn1str )
        return buf.read_all()

    def __del__(self):
        try:
            if self._pyfree:
                m2.asn1_string_free(self.asn1str)
        except AttributeError:
            pass
                                                                                                        
    def _ptr(self):
        return self.asn1str


class ASN1_Object:
    def __init__(self, asn1obj, _pyfree=0):
        self.asn1obj = asn1obj
        self._pyfree = _pyfree

    def __del__(self):
        try:
            if self._pyfree:
                m2.asn1_object_free(self.asn1obj)
        except AttributeError:
            pass

    def _ptr(self):
        return self.asn1obj


class ASN1_UTCTIME:
    def __init__(self, asn1_utctime=None, _pyfree=0):
        if asn1_utctime is not None:
            assert m2.asn1_utctime_type_check(asn1_utctime), "'asn1_utctime' type error'"
            self.asn1_utctime = asn1_utctime
            self._pyfree = _pyfree
        else:
            self.asn1_utctime = m2.asn1_utctime_new ()
            self._pyfree = 1

    def __del__(self):
        try:
            if self._pyfree:
                m2.asn1_utctime_free(self.asn1_utctime)
        except AttributeError:
            pass

    def __str__(self):
        assert m2.asn1_utctime_type_check(self.asn1_utctime), "'asn1_utctime' type error'"
        buf = BIO.MemoryBuffer()
        m2.asn1_utctime_print( buf.bio_ptr(), self.asn1_utctime )
        return buf.read_all()

    def _ptr(self):
        assert m2.asn1_utctime_type_check(self.asn1_utctime), "'asn1_utctime' type error'"
        return self.asn1_utctime

    def set_string (self, string):
        assert m2.asn1_utctime_type_check(self.asn1_utctime), "'asn1_utctime' type error'"
        return m2.asn1_utctime_set_string( self.asn1_utctime, string )

    def set_time (self, time):
        assert m2.asn1_utctime_type_check(self.asn1_utctime), "'asn1_utctime' type error'"
        return m2.asn1_utctime_set( self.asn1_utctime, time )

