set term pdfcairo font "Monofur"
set out "Sw.pdf"
set xdata time
set timefmt "%s"
set format x "%d %b"
file = "../postProcessing/probes/0/Sw"
set xlabel "Time"
set ylabel "Water Saturation"
set yrange [0:1]
set xtics rotate
t = "`pwd | rev | cut -f 2 -d '/' | rev | cut -f 2 -d 't'`"
set title "Scenario: Five Spot ".t

plot file skip 1 u 1:2 smooth bezier w l lw 3 t "Producer-Sw",\
file skip 1 u 1:3 smooth bezier w l lw 3 t "Injector1-Sw",\
file skip 1 u 1:4 smooth bezier w l lw 3 t "Injector2-Sw"
set term wxt persist
replot
