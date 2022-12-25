function isPalindrome(x: number): boolean {    
    if(x < 0) return false
    if(x > 0 && x % 10 == 0) return false
    if(x == 0) return true

    let palNum:number = 0;
    let lastDigit:number;
    let realNum:number = x;

    while(x != 0){
        lastDigit = x % 10 
        palNum = palNum * 10 + lastDigit 
        x = Math.floor(x / 10)
    }
    
    if(palNum % realNum == 0){
        return true
    } else {
        return false
    }
};