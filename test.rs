fn test_divisibility_by_3_4(a:i32) -> i32{
    let mut b:i32 = -10;
    if a % 3 == 0 && a%4 == 0{
        b = 0
    }
    else if a % 3 == 0{
        b = 1
    }
    else if a % 4 == 0{
        b = 2
    }
    else {
        b = -1
    }
    b
}