set term pdfcairo font "Monofur"
set out "BHP.pdf"
set xdata time
set timefmt "%s"
set format x "%d %b"
file = "../postProcessing/probes/0/p"
set xlabel "Time"
set ylabel "Pressure [Psi]"
set xtics rotate
t = "`pwd | rev | cut -f 2 -d '/' | rev | cut -f 2 -d 't'`"
set title "Scenario: Five Spot ".t

plot file skip 1 u 1:($2/6894.75) smooth bezier w l lw 3 t "Producer-BHP",\
file skip 1 u 1:($3/6894.75) smooth bezier w l lw 3 t "Injector-BHP"
set term wxt persist
replot
