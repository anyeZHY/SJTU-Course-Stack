% Reference: 
% https://stackoverflow.com/questions/30125908
% Then I know how to use profile('info').FunctionTable(1).TotalTime
arr = rand(2^24,1);
A = gpuArray(arr);
T1 = zeros(3,1);
T2 = zeros(3,1);
T3 = zeros(6,1);
T4 = zeros(6,1);
N=20;
for j = 1:N
    for i = 4:4:24
    if i<13
        profile on
        naive_fft(arr(1:2^i));
        profile off
        T1(i/4) = T1(i/4) + profile('info').FunctionTable(1).TotalTime;

        profile on
        mat_fft(arr(1:2^i));
        profile off
        T2(i/4) = T2(i/4) + profile('info').FunctionTable(1).TotalTime;
    end
    
    profile on
    fft(arr(1:2^i));
    profile off
    T3(i/4) = T3(i/4) + profile('info').FunctionTable(1).TotalTime;

    profile on
    fft(A(1:2^i));
    profile off
    T4(i/4) = T4(i/4) + profile('info').FunctionTable(1).TotalTime;
    end
end
T1 = T1./N;
T2 = T2./N;
T3 = T3./N;
T4 = T4./N;

%% Visualization
x1 = 4:4:12;
% x1 = 2.^x1;
x2 = 4:4:24;
% x2 = 2.^x2;

semilogy(x1,T1,'LineWidth',1);
hold on
semilogy(x1,T2,'LineWidth',1);
semilogy(x2,T3,'LineWidth',1);
semilogy(x2,T4,'LineWidth',1);
% xlabel('$\log_2$',Interpreter='latex');
% ylabel('$\log_{10}$',Interpreter='latex');
legend('For','Matrix','FFT','GPU');
hold off




%% Functions
function out = mat_fft(x)
N = length(x);
unit = exp(-1i*2*pi/N);
unit_x = ones(N,1);
for i = 2:N
    unit_x(i) = unit_x(i-1) * unit;
end
M = ones(N,N);
for i = 2:N
    M(i,:) = M(i-1,:) .* unit_x.';
end
out = M * x;
end

function out = naive_fft(x)
N = length(x);
out = zeros(N,1);
for k = 1:N
    for j = 1:N
        out(k) = out(k) + x(j)*exp(-1i*(k-1)*(j-1)*2*pi/N);    
    end
end
end