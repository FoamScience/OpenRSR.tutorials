# gnuplot script to plot font displacement
do for [t=100:800:100] {\
    set term pdfcairo enhanced
    set out 'front-'.t.'.pdf'
    file = ''.t.'.dat'
    set xlabel 'Length (m)'
    set ylabel 'S_w'
    set title "Bucklet-Leverett, day: ".t
    plot file u 1:2 w l t "Capillary Effects", '' u 1:3 w l t "No Capillarity"
    set term wxt
}

