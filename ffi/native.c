/* IL-3 FFI/native — shared native-side STUB documenting the sink.
 *
 * The point of the IL-3 fixtures is whether the engine flags the unvalidated
 * value *reaching* the FFI call on the managed side — NOT analysis of this C body
 * (per research/cross-language-interop-plan.md §IL-3). This file is the sink that
 * every managed caller (ctypes/JNI/cgo/N-API/extern-C) ultimately invokes.
 */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* SINK (CWE-78): tainted string from the managed runtime reaches system(). */
int run_cmd(const char *cmd) {
    return system(cmd);
}

/* SINK (CWE-787): unbounded copy into a fixed stack buffer. */
void copy_in(const char *src) {
    char buf[64];
    strcpy(buf, src);   /* no bounds check */
    printf("%s\n", buf);
}
