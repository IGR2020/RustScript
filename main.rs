use std::io;

fn main() {
    let mut l = 39;
    println!("hello world");
    let mut x = 9;
    println!("no");
    let mut y = 90;
    println!("{}", x);
    y += 90;
    println!("{}", y);
    if y > x {
        println!("y better");
        println!("p");
        if y > x {
            println!("r");
        }
    }
}
