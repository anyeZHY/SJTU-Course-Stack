N_Const= 2000; % paddings
L = 101; % length
sample = 4; % requirement : even; (N_const//sample)*sample == N_const
order = 9;
Wn = 0.1;
x = (1:1:N_Const);

%% >>>>>>>> Problem 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
origin = zeros(1,N_Const);
origin(1:L) = 1;

sampled_1 = origin(1:sample:end);
F1 = abs(fftshift(fft(sampled_1)));

%% >>>>>>>> Problem 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
shiftted = origin;
shiftted(1:sample/2) = 0;
shiftted(L+1:L+1+sample/2) = 1;

sampled_2 = shiftted(1:sample:end);
F2 = abs(fftshift(fft(sampled_2)));

%% >>>>>>>> Problem 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[b,a] = butter(order, Wn);
filt = filtfilt(b,a,shiftted);

sampled_3 = filt(1:sample:end);
F3 = abs(fftshift(fft(sampled_3)));



%% Visualization
sw_vi = 1;
if (sw_vi)
    % Time
    k=150;
    linewidth=1.8;
    sample_x = (1:sample:N_Const);
    
    gcf = figure;
    hold on;
    plot(x(1:k),origin(1:k),'b-', ...
        sample_x(1:k/sample),sampled_1(1:k/sample),'ro', ...
        LineWidth=linewidth);
    stem(sample_x(1:k/sample),sampled_1(1:k/sample),'r',LineWidth=linewidth);
    ylim([0,1.1]);
    savefig('p1_time.fig');
%     saveas(gcf,'p1_time.eps','psc2');
    print('-depsc','p1_time.eps');
    hold off;
    
    gcf = figure;
    hold on;
    plot(x(1:k),shiftted(1:k), ...
        'b-',sample_x(1:k/sample),sampled_2(1:k/sample),'ro', ...
        LineWidth=linewidth);
    stem(sample_x(1:k/sample),sampled_2(1:k/sample),'r',LineWidth=linewidth);
    ylim([0,1.1]);
    savefig('p2_time.fig');
%     saveas(gcf,'p2_time.eps','psc2');
    print('-depsc','p2_time.eps');
    hold off;
    
    gcf = figure;
    hold on;
    plot(x(1:k),filt(1:k),'b-', ...
        sample_x(1:k/sample),sampled_3(1:k/sample),'ro', ...
        LineWidth=linewidth);
    stem(sample_x(1:k/sample),sampled_3(1:k/sample),'r',LineWidth=linewidth);
    ylim([-0.1,1.15]);
    savefig('p3_time.fig');
%     saveas(gcf,'p3_time.eps');
    print('-depsc','p3_time.eps');
    hold off;
    
    % Spectrum
    l=length(F1);
    gcf = figure;
    plot(x(1:l),F1,x(1:l),F2,x(1:l),F3,LineWidth=1.2);
    xlim([160,340])
    legend('original','shiftted','filtered');
    savefig('spectrum.fig');
%     saveas(gcf,'spectrum.eps');
    print('-depsc','spectrum.eps');

    gcf = figure;
    plot(x(1:l),F1,x(1:l),F2,x(1:l),F3,LineWidth=1.8);
    xlim([50,210])
    legend('original','shiftted','filtered');
    savefig('spectrum_prime.fig');
%     saveas(gcf,'spectrum_prime.eps');
    print('-depsc','spectrum_prime.eps');

    gcf = figure;
    plot(x(1:l),F1,x(1:l),F2,x(1:l),F3,LineWidth=1.8);
    ylim([18,28])
    legend('original','shiftted','filtered');
    savefig('spectrum_prime2.fig');
%     saveas(gcf,'spectrum_prime2.eps');
    print('-depsc','spectrum_prime2.eps');
end