% Make the following assumptions:
% (1) Restrict values of x to the interval [-7,7].
% (2) Population size = 10
% (3) Probability of crossover = 0.6 (i.e., 60%)
% (4) Probability of mutation = 0.05 (i.e., 5%)
% (5) Enable elitism by automatically carrying the top 2 designs to the next generation.
% (6) Use a random initial population.
% (7) Use at least 6 binary bits to encode the variable.

% GA Problem Setup
% Coding the variables: continuous or discrete?
cont = input('Continuous or discrete variables? Input "C" or "D": ', 's');
while strcmp(cont, 'C') == 0 && strcmp(cont, 'D') == 0
    cont = input('Continuous or discrete variables? Input "C" or "D": ', 's');
end
if strcmp('C', cont)
    domain = input('Enter interval in bracket notation: ');
else 
    num_discrete = input('Enter number of discrete variables desired: ');
    if num_discrete % 2 %if discrete values are odd, apply ceiling funct
        total_bits = ceil(log2(num_discrete));
    else
        total_bits = log2(num_discrete);
    end
end