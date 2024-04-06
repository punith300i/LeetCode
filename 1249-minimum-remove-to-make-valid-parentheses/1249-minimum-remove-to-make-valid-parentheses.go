func minRemoveToMakeValid(s string) string {
    stack := []byte{}
    result := make([]byte, 0, len(s))
    for i, _ := range s{
        if len(stack)==0 && s[i]==')'{
            continue
        }
        
        if s[i]=='('{
            stack = append(stack, s[i])
        }else if len(stack)>0 && s[i]==')'{
            stack = stack[:len(stack)-1]
        }
        
        result = append(result, s[i])
    }
    
    if len(stack)>0{
        for i:=len(result)-1; i>-1; i--{
            if result[i]=='('{
                result = append(result[:i], result[i+1:]...)
                stack = stack[:len(stack)-1]
            }
            if len(stack)==0{
                break
            }
        }
    }
    
    return string(result)
}