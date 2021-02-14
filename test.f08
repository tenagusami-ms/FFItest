! Created by ykanya on 2021/02/13.
module test_module
   use iso_c_binding
   implicit none
   contains
    integer(c_int) function test2(i) bind(C)
        integer(c_int), intent(in), value :: i
        integer(c_int) :: this
        this = i + 1
    end function test2
end module test_module

subroutine test(i) bind(C)
    use iso_c_binding
    implicit none
    integer(c_int), intent(in), value :: i
    ! integer(c_int) :: test
    write(*,*) i
    ! test=i
end subroutine test
