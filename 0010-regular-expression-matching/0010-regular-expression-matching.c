bool isMatch(char * s, char * p) {
    if (*p == '\0') {
        return *s == '\0';
    }
    
    bool match = (*s != '\0' && (*p == *s || *p == '.'));
    
    if (*(p + 1) == '*') {
        return isMatch(s, p + 2) || (match && isMatch(s + 1, p));
    }
    
    return match && isMatch(s + 1, p + 1);
}