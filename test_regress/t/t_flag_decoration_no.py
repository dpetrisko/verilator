#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# Copyright 2024 by Wilson Snyder. This program is free software; you
# can redistribute it and/or modify it under the terms of either the GNU
# Lesser General Public License Version 3 or the Perl Artistic License
# Version 2.0.
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('vlt')
test.top_filename = "t/t_flag_decoration.v"

test.compile(verilator_flags2=["--no-decoration"])

test.file_grep(test.obj_dir + "/V" + test.name + ".h", r'\n// CONSTRUCTORS')
test.file_grep_not(test.obj_dir + "/V" + test.name + ".h", r'\n    // CONSTRUCTORS')
test.file_grep_not(test.obj_dir + "/V" + test.name + ".h", r'/\*t/t_flag_decoration')

test.passes()