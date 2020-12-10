
def playsong()
    song = Music.new('IHVMK.mp3')
    puts "Starting song", "\n"
    song.play
    song.loop = true
    puts "Playing song", "\n"
end

playsong()