from rich import print
import utility.utility as util

def main():
  print("""
  [cyan]==========================================================================[/cyan]
                                                                                   
   ____                                     ___    _____                           
  |    \ _ _ ___ ___ ___ ___ ___ ___    ___|  _|  |   __|___ ___ _____ ___ ___ ___ 
  |  |  | | |   | . | -_| . |   |_ -|  | . |  _|  |  |  | . |  _|     | . | . | -_|
  |____/|___|_|_|_  |___|___|_|_|___|  |___|_|    |_____|__,|_| |_|_|_|__,|_  |___|
                |___|                                                     |___|

  You stand at the gates of a [purple]mysterious[/ purple] dungeon, Do you wish to enter\?
  [cyan]=============================================================================[/cyan]
  """)
  #Game starts here 
  util.start()

main()