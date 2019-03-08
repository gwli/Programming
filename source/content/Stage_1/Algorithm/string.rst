字符串的处理
###########

#。 字符串表示 '', ""

常用操作
========
   
   * 单串
     
     * 长度
     * 拼接 
     * split
     * index/slice
     * search (forword/backword)
     * substr
     * regexpr
     * cp
  
  * 双串
     * eq
     * sort
     * diff
     * edit distance
     
  * 格式化的字符串
     {prefix:pading,align,pricse}
     
     .. code-block:: bash
     
        format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
        fill            ::=  <any character>
        align           ::=  "<" | ">" | "=" | "^"
        sign            ::=  "+" | "-" | " "
        width           ::=  digit+
        grouping_option ::=  "_" | ","
        precision       ::=  digit+
        type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
 
 * 时间字符串
