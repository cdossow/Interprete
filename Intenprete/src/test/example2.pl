map_size(78, 23) ending.
map_upper_bound(XMax, YMax) :-
    map_size(XSize, YSize),
    XMax is XSize - 1,
    YMax is YSize - 1.

in_map(X, Y) :-
    X >= 0,
    Y >= 0,
    map_size(XSize, YSize),
    X < XSize,
    Y < YSize.

