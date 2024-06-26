class DarkMode:
    def __init__(self, app):
        self.app = app
        self.app.configure(bg='#1c1c1c')
        self.app.option_add('*Font', 'Helvetica 12')
        self.app.option_add('*Button.Background', '#1c1c1c')
        self.app.option_add('*Button.Foreground', '#ffffff')
        self.app.option_add('*Button.ActiveBackground', '#1c1c1c')
        self.app.option_add('*Button.ActiveForeground', '#ffffff')
        self.app.option_add('*Button.DisabledBackground', '#1c1c1c')
        self.app.option_add('*Button.DisabledForeground', '#ffffff')
        self.app.option_add('*Button.HighlightBackground', '#1c1c1c')
        self.app.option_add('*Button.HighlightForeground', '#ffffff')
        self.app.option_add('*Button.Border', '#1c1c1c')
        self.app.option_add('*Button.Relief', 'flat')
        self.app.option_add('*Button.OverRelief', 'flat')
        self.app.option_add('*Button.Underline', '-1')
        self.app.option_add('*Button.FocusColor', '#1c1c1c')
        self.app.option_add('*Button.FocusBorder', '#1c1c1c')
        self.app.option_add('*Button.SelectColor', '#1c1c1c')
        self.app.option_add('*Button.SelectBorder', '#1c1c1c')
        self.app.option_add('*Button.Padding', '0')
        self.app.option_add('*Button.BorderWidth', '0')
        self.app.option_add('*Button.HighlightThickness', '0')
        self.app.option_add('*Button.FocusThickness', '0')
        self.app.option_add('*Button.SelectBorderWidth', '0')
        self.app.option_add('*Button.SelectForeground', '#ffffff')
        self.app.option_add('*Button.SelectBackground', '#1c1c1c')
        self.app.option_add('*Button.Default', '#1c1c1c')
        self.app.option_add('*Button.DefaultBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultForeground', '#ffffff')
        self.app.option_add('*Button.DefaultBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultActiveForeground', '#ffffff')
        self.app.option_add('*Button.DefaultActiveBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultDisabledForeground', '#ffffff')
        self.app.option_add('*Button.DefaultDisabledBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultHighlightForeground', '#ffffff')
        self.app.option_add('*Button.DefaultHighlightBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultSelectForeground', '#ffffff')
        self.app.option_add('*Button.DefaultSelectBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultFocusForeground', '#ffffff')
        self.app.option_add('*Button.DefaultFocusBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultActiveBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultActiveRelief', 'flat')
        self.app.option_add('*Button.DefaultActiveOverRelief', 'flat')
        self.app.option_add('*Button.DefaultActiveUnderline', '-1')
        self.app.option_add('*Button.DefaultActiveHighlightThickness', '0')
        self.app.option_add('*Button.DefaultActiveFocusThickness', '0')
        self.app.option_add('*Button.DefaultActiveSelectBorderWidth', '0')
        self.app.option_add('*Button.DefaultActiveSelectForeground', '#ffffff')
        self.app.option_add('*Button.DefaultActiveSelectBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultDisabledBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultDisabledRelief', 'flat')
        self.app.option_add('*Button.DefaultDisabledOverRelief', 'flat')
        self.app.option_add('*Button.DefaultDisabledUnderline', '-1')
        self.app.option_add('*Button.DefaultDisabledHighlightThickness', '0')
        self.app.option_add('*Button.DefaultDisabledFocusThickness', '0')
        self.app.option_add('*Button.DefaultDisabledSelectBorderWidth', '0')
        self.app.option_add('*Button.DefaultDisabledSelectForeground', '#ffffff')
        self.app.option_add('*Button.DefaultDisabledSelectBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultHighlightBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultHighlightRelief', 'flat')
        self.app.option_add('*Button.DefaultHighlightOverRelief', 'flat')
        self.app.option_add('*Button.DefaultHighlightUnderline', '-1')
        self.app.option_add('*Button.DefaultHighlightHighlightThickness', '0')
        self.app.option_add('*Button.DefaultHighlightFocusThickness', '0')
        self.app.option_add('*Button.DefaultHighlightSelectBorderWidth', '0')
        self.app.option_add('*Button.DefaultHighlightSelectForeground', '#ffffff')
        self.app.option_add('*Button.DefaultHighlightSelectBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultSelectBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultSelectRelief', 'flat')
        self.app.option_add('*Button.DefaultSelectOverRelief', 'flat')
        self.app.option_add('*Button.DefaultSelectUnderline', '-1')
        self.app.option_add('*Button.DefaultSelectHighlightThickness', '0')
        self.app.option_add('*Button.DefaultSelectFocusThickness', '0')
        self.app.option_add('*Button.DefaultSelectSelectBorderWidth', '0')
        self.app.option_add('*Button.DefaultSelectSelectForeground', '#ffffff')
        self.app.option_add('*Button.DefaultSelectSelectBackground', '#1c1c1c')
        self.app.option_add('*Button.DefaultFocusBorder', '#1c1c1c')
        self.app.option_add('*Button.DefaultFocusRelief', 'flat')
        self.app.option_add('*Button.DefaultFocusOverRelief', 'flat')
        self.app.option_add('*Button.DefaultFocusUnderline', '-1')
        self.app.option_add('*Button.DefaultFocusHighlightThickness', '0')
        self.app.option_add('*Button.DefaultFocusFocusThickness', '0')
        self.app.option_add('*Button.DefaultFocusSelectBorderWidth', '0')


