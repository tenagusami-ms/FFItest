from cffi import FFI


def main() -> None:

    ffi_builder = FFI()

    # ヘッダ情報をincludeする
    # ffi_builder.set_source("test", """
    # #include "test.h"
    # """, libraries=["test"])

    # Python化したいC関数の定義を記述する
    ffi_builder.cdef(
        "void test(int);"
        "int test2(int);")
    lib = ffi_builder.dlopen("cmake-build-debug/libtest.so")

    lib.test(1)
    print(lib.test2(2))


if __name__ == "__main__":
    main()
