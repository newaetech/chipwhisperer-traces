from script_common import *

scope = cw.scope(name="Husky")
target = cw.target(scope, cw.targets.SimpleSerial2)

scope.default_setup()
build_copy_prog_fw(scope, "simpleserial-aes")

# TODO: add method of replacing C files temporarily for build