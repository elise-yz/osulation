% Data for different version models
versions = {'Version 1', 'Version 2', 'Version 3', 'Version 4', 'Version 5', 'Version 6'};
accuracy_clicking = [0.60, 0.75, 0.78, 0.90, 0.76, 0.92];
accuracy_holding = [0.55, 0.70, 0.72, 0.85, 0.74, 0.88];
timing_to_register = [1.5, 1.2, 1.3, 0.8, 1.1, 0.7];

% Create a table
data_table = table(versions', accuracy_clicking', accuracy_holding', timing_to_register', ...
                   'VariableNames', {'Version', 'Accuracy_Clicking', 'Accuracy_Holding', 'Timing_Register'});
disp(data_table);

% Bar graph for accuracy
figure;
hold on;
% Using categorical for x-axis
x_categorical = categorical(data_table.Version);
bar(x_categorical, [data_table.Accuracy_Clicking, data_table.Accuracy_Holding], 'grouped', 'FaceColor', 'flat');

% Customize bar colors
b = gca;
b.Children(1).FaceColor = [0.2, 0.6, 1]; % Clicking Accuracy
b.Children(2).FaceColor = [1, 0.4, 0.2]; % Holding Accuracy

set(gca, 'XTickLabel', data_table.Version);
title('Model Accuracy Comparison', 'FontSize', 14, 'FontWeight', 'bold');
xlabel('Version', 'FontSize', 12);
ylabel('Accuracy', 'FontSize', 12);
legend({'Clicking Accuracy', 'Holding Accuracy'}, 'Location', 'Best');
grid on; % Add grid lines for better readability
set(gca, 'YLim', [0 1]); % Set Y limits to keep it consistent
hold off;

% Line plot for timing
figure;
plot(x_categorical, data_table.Timing_Register, '-o', 'LineWidth', 2, 'MarkerSize', 8, 'Color', [0.3, 0.8, 0.3], 'DisplayName', 'Timing to Register');
title('Timing to Register Comparison', 'FontSize', 14, 'FontWeight', 'bold');
xlabel('Version', 'FontSize', 12);
ylabel('Timing to Register (s)', 'FontSize', 12);
grid on; % Add grid lines
set(gca, 'YLim', [0 2]); % Set Y limits for clarity
hold off;
