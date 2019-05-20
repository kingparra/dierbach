*******************************************
 Figure 3-11: Compound Statement in Python
*******************************************

 ::

     +
              +>   if which == 'F':                             <-- header     <+
      first  -+>       converted_temp = (temp - 32) * 5/9       <+             <+
      clause -+>       print(temp, 'degrees Fahrenheit equals', <+- suite      <+
              +>             converted_temp, 'degrees Celsius') <+             <+-  control
                +> else:                                           <-- header  <+- structure
                +>     converted_temp = (9/5 * temp) + 32          <+          <+
        second -+>                                                 <+- suite   <+
        clause -+>     print(temp, 'degrees Celsius equals',       <+          <+
                +>           converted_temp, 'degrees Fahrenheit') <+          <+

  from Ch 3, 3.3.2 Indentation in Python, page 90

