#! /usr/bin/octave-cli -qf
arg_list = argv ();

for i =1:nargin
    printf('Sparsness for %s \n', arg_list{i});
    M = load(arg_list{i});
    S = spconvert(M)
    spy(S)
    pause
end
