! compiled by:
! gfortran -shared -fPIC test.f90 -o ftest.so

subroutine sub(n, arr, x, ans) bind(c, name='sub')
    use iso_c_binding, only: c_int, c_float      ! must use C types to declare variables
    implicit none
    integer(c_int), intent(in) :: n
    real(c_float), intent(in) :: arr(n), x
    real(c_float), intent(out) :: ans
    integer(c_int) :: i
    
    do i = 1, n
        ans = ans + arr(i)
    end do
    ans = ans * x
    
    return
end subroutine sub


function func(n, arr, x) bind(c, name='func')
    use iso_c_binding, only: c_int, c_float
    implicit none
    integer(c_int), intent(in) :: n
    real(c_float), intent(in) :: arr(n), x
    real(c_float) :: func
    integer(c_int) :: i
    
    func = 0.
    do i = 1, n
        func = func + arr(i)
    end do
    func = func * x
    
    return
end function func
    