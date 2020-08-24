import os, sys
try:
    import pafy # youtube downloader api
except:
    print('pafy not found\ntype "pip install pafy" and "pip install youtube_dl" then run again')
    sys.exit()

class YouTubeDownLoader():
    # making and obj of pafy and starting the bot
    def __init__(self, whole_url):
        self.explicit_url = ''
        if '=' not in whole_url:
            self.explicit_url = whole_url.split('\\')[-1]
        else:
            self.explicit_url = whole_url.split('=')[-1]
        self.video = pafy.new(self.explicit_url)
        self.choose_method()

    
    # for when the wrong input is entered
    def wrong_input(self):
        print('wrong input!')
        sys.exit()


    def nothing_found(self):
        print('nothing found')
        sys.exit()


    # choose the method and doing the stuff
    def choose_method(self):
        text = '''
download:
1.video-only
2.audio-only
3.both (embeded)
4.both (separately)
which one? (1/2/3/4) '''

        try:
            method = int(input(text).strip())
        except:
            self.wrong_input()
        
        if method==1:
            self.parse_video()
        elif method==2:
            self.parse_audio()
        elif method==3:
            self.parse_both_emb()
        else:
            self.parse_both_sep()


    # chooses one stream and downloads it
    def download(self, all_streams):
        # nothing found
        if len(all_streams)==0:
            self.nothing_found()
        else:
            # for input's text
            i_s = []
            print('\n\nall that found:')
            for i in range(len(all_streams)):
                strm = (str(all_streams[i]).split(':')[-1]).split('@')
                print(f'{i+1}. {strm[0]}, {strm[1]}')
                i_s.append(i+1)
            text = '\nwhich one?('+'/'.join([str(i) for i in i_s])+') '
            # checking if the user didn't enter wrong input
            try:
                which = int(input(text).strip())
            except:
                self.wrong_input()
            
            # downloading the chosen format of video
            try:
                all_streams[which-1].download()
            except:
                print('\nsomething went wrong downloading this!')


    # parsing the video-only
    def parse_video(self):
        # all the possible formats
        all_streams = self.video.videostreams
        # download the shit
        self.download(all_streams)


    # parsing the audio only
    def parse_audio(self):
        all_streams = self.video.audiostreams
        self.download(all_streams)


    # parsing both video and audio embeded to one single file
    def parse_both_emb(self):
        all_streams = self.video.streams
        self.download(all_streams)


    # parsing both video and audio seperately
    def parse_both_sep(self):
        print('\n\n****Audio Part****')
        self.parse_audio()
        print('\n\n****Audio Part****')
        self.parse_video()





if __name__ == "__main__":
    # make the downloads folder and cd to that
    if not os.path.isdir('downloads'):
        os.system('mkdir downloads')
    os.chdir('downloads')

    # if url is passed through argument start the bot
    args = sys.argv
    if len(args)==1:
        print('you have to pass the url via argument')
    elif len(args)==2:
        ytdl = YouTubeDownLoader(args[1])
    else:
        print('too many argument bruh')
        sys.exit()