% Initialization
filename = 'Justin Timberlake,Carey Mulligan,Stark Sands - Five Hundred Miles.mp3';
[y,Fs] = audioread(filename);
L = 2200000;
audio = y(1:L);
% sound(audio,Fs)

save = 1; % used to activate 
%% ===== Problem 1, 2 and 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if save
    subplot(2,2,[1 2])
    plot(audio)
    subplot(2,2,[3,4])
    stft(audio)
    print('-depsc',"origin.eps");
    
    for f = (5000:5000:15000)
        figure;
        audio_ds = resample(audio, f, Fs);
        subplot(2,2,[1 2])
        plot(audio_ds)
        title("downsample, $f=$"+f, Interpreter="latex")
        subplot(2,2,[3,4])
        stft(audio_ds)
        filename_tmp = "downsample_"+ f +".wav";
        audiowrite(filename_tmp, audio_ds, f)
        print('-depsc',"downsample_"+ f +".eps");
    
        figure;
        pos = linspace(1,length(audio_ds),L);
        audio_itr = interp1(audio_ds, pos);
        subplot(2,2,[1 2])
        plot(audio_itr)
        title("interpolate, $f=$"+f, Interpreter="latex")
        subplot(2,2,[3,4])
        stft(audio_itr)
        filename_tmp = "interpolate_"+ f +".wav";
        audiowrite(filename_tmp, audio_itr, Fs)
        print('-depsc',"interpolate_"+ f +".eps");
    end
end

%% ===== Problem 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
% 1: lowpass
% 2: highpass
% 3: bandpass
% 4: bandstop
mode = 3;
f1 = 2/Fs*100;
f2 = 2/Fs*1000;
order = 1;
if mode == 1
    [b,a] = butter(order, f1);
elseif mode == 2
    [b,a] = butter(order, f2, 'high');
elseif mode == 3
    [b,a] = butter(order, [f1 f2]);
else
    [b,a] = butter(order, [f1 f2], 'stop');
end
filt = filtfilt(b,a,audio) * 2;
audiowrite("filt.wav", filt, Fs)
% figure
% subplot(2,1,1)
% pspectrum(audio)
% figure
% freqz(b,a)
% subplot(2,1,2)
% pspectrum(filt)
% diff = [filt(1:300000), audio(1:300000), filt(600000:1100000), audio(600000:1100000)];
% sound(diff, Fs)