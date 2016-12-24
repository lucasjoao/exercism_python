class Clock:
  def to_hours(self, hours):
    if hours >= 24:
      return hours % 24
    elif hours < 0:
      hours = abs(hours)
      if hours >= 24:
        return 24 - (hours % 24)

      return 24 - hours

    # between 0 and 24
    return hours

  def to_minutes(self, minutes):
    if minutes >= 60:
      self.fix_hours(minutes, True, False)
      return minutes % 60
    elif minutes < 0:
      minutes = abs(minutes)
      if minutes >= 60:
        self.fix_hours(minutes, False, False)
        return 60 - (minutes % 60)

      self.fix_hours(60, False, True)
      return 60 - minutes

    # between 0 and 60
    return minutes

  def fix_hours(self, minutes, positive, gambiarra):
    hours_in_minutes = minutes - (minutes % 60)
    hours = hours_in_minutes / 60

    if positive:
      self.hours += self.to_hours(hours)
    elif not positive and gambiarra:
      self.hours -= 1
    elif not positive:
      self.hours -= self.to_hours(hours+1)

    self.hours = self.to_hours(self.hours)

  def add(self, minutes):
    self.minutes += minutes
    self.minutes = self.to_minutes(self.minutes)
    return self

  def __init__(self, hours, minutes):
    self.hours = self.to_hours(hours)
    self.minutes = self.to_minutes(minutes)

  def __str__ (self):
    return '{}:{}'.format(str(self.hours).zfill(2), str(self.minutes).zfill(2))

  def __eq__ (self, other):
    return self.hours == other.hours and self.minutes == other.minutes
