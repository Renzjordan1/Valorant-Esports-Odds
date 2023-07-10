#Team Class
class Team:

  def __init__(self, name, econ, prevEcon, WS, deaths, wins):
    self.name = name
    self.econ = econ
    self.prevEcon = prevEcon
    self.WS = WS  #WS = Win Streak
    self.deaths = deaths
    self.wins = wins

  #Reset Econ to Pistol round
  def reset_econ(self):
    self.econ = 800
    self.prevEcon = 800
    self.WS = 0

  def set_deaths(self, enemyKillCreds):
    self.deaths = enemyKillCreds/200

  def set_prevEcon(self):
    self.prevEcon = self.econ

  def set_wins(self, win):

    if(win):
      self.WS += 1
      self.wins += 1

    else:
      self.WS = 0




