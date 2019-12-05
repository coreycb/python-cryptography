# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/obj_mac.h>
"""

TYPES = """
static const int Cryptography_HAS_X25519;
static const int Cryptography_HAS_X448;
static const int Cryptography_HAS_ED448;
static const int Cryptography_HAS_ED25519;

static const int NID_undef;
static const int NID_pbe_WithSHA1And3_Key_TripleDES_CBC;
static const int NID_X25519;
static const int NID_X448;
static const int NID_ED25519;
static const int NID_ED448;

static const int NID_subject_alt_name;
static const int NID_crl_reason;
"""

FUNCTIONS = """
"""

CUSTOMIZATIONS = """
#ifndef NID_X25519
static const long Cryptography_HAS_X25519 = 0;
static const int NID_X25519 = 0;
#else
static const long Cryptography_HAS_X25519 = 1;
#endif
#ifndef NID_ED25519
static const long Cryptography_HAS_ED25519 = 0;
static const int NID_ED25519 = 0;
#else
static const long Cryptography_HAS_ED25519 = 1;
#endif
#ifndef NID_X448
static const long Cryptography_HAS_X448 = 0;
static const int NID_X448 = 0;
#else
static const long Cryptography_HAS_X448 = 1;
#endif
#ifndef NID_ED448
static const long Cryptography_HAS_ED448 = 0;
static const int NID_ED448 = 0;
#else
static const long Cryptography_HAS_ED448 = 1;
#endif
"""