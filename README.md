This repo contains the files for the "Network Forensics Workshop Deux: Long Live Packet Pillaging" workshop, which will be held at CactusCon 2016 (http://www.cactuscon.com/ryan-chapman).

README.md v0.1 -- If this number changes, go check the change log :)

---

# Workshop Details

In the workshop, I will walk attendees through how Bechtel’s "Team Threat Level Pancakes" (formerly "Team DOFIR") took 1st place in LMG Security’s Network Forensics Puzzle Contest (NFPC) at DefCon 23 (2015). This was a repeat win for us, and we enjoyed every minute that we have spent on these challenges. LMG holds an awesome annual contest, and we are proud to show the tech that we used to complete the most recent challenge. Keep in mind that this is a "WE" thing. I put together the workshop, but OUR TEAM wins these things. I am honored to work with such awesome people.

To solve the sucker, we used tools such as Wireshark, NetworkMiner, bash, volatility, Python, and others. I cover how we put together some scripts and commands in order to streamline our methodology. My goal: Show off some cool network forensics tech and garner interest for yet another NFPC. We want some top-notch competition, so check out what we have to offer and be sure to get your game on at DefCon 24 in 2016!

---

# Requirements

I recommend that you use Kali Linux v2.0+.  See here: https://www.kali.org/downloads/.  If you are using Kali, you will still need to download some additional tools to your distro.  If you are not using Kali, well then you have your work cut out for you!

For the workshop, please install the following tools:

- *bless* – Great nix-based hex editor
- *Audacity* – Audio playing/editing program with the ability to play audio files in reverse (see Round 3)
- *tcplay* – Free and simple TrueCrypt Implementation based on dm-crypt (see Round 6)

You can install all three in Kali using the following command:

**sudo apt-get install bless audacity tcplay**

## NetworkMiner

Last year, I made a point to avoid NetworkMiner.  This year, our intern showed us that easy-of-use tools such as NetworkMiner might be required in these challenges.  Hah!

We will *need* NetworkMiner (NM) to complete Round 3.  You can grab NM here: http://www.netresec.com/?page=NetworkMiner.  Feel free to run NM under Windows, either in your host OS or within a Windows-based VM.

Personally, I like to run NM under Kali using mono.  For details, see here: http://www.netresec.com/?page=Blog&month=2011-12&post=No-more-Wine---NetworkMiner-in-Linux-with-Mono.

If you want to run NM under Kali, please visit the above link and set this up prior to the workshop.

## Non-Kali Requirements

Many of the tools that you will need for this workshop are bundled with Kali 2.x.  For those not using Kali, please make sure that you have the following tools available in addition to those listed above:

- Wireshark (1.12.x preferred; please only use 2.0 if you are familiar with all GUI-based changes)
- Python (2.6 preferred -- avoid 3.0 'cause reasons)
- Volatility 2.4+ (http://www.volatilityfoundation.org/ -- we'll be using 2.4)
- foremost (http://foremost.sourceforge.net/)
- aircrack-ng (http://www.aircrack-ng.org/)

---

# Obtaining the Files

At CactusCon 2016, I will be handing out 40 copies of LMG Security's Network Forensics Puzzle Challenge 2015 DVD.  If you receive one, and you have a DVD drive, great!

Additionally, I will have a WNDR3700 router setup along with a switch.  The relevant files will be available via a local network share on this private network.  Be sure to bring a network adapter if you don't have one built-in, and be sure to bring an Ethernet cable too (heck, bring a few and share).

If CactusCon '16 is over, and you did not receive the associated PCAP files at the conference, FEAR NOT!  Please contact me for details or go directly to the source: LMG Security (@LMGSecurity).

## Passwords

The TrueCrypt volumes on the official LMG Security DVD require passwords.
Please note that zeroes are often used instead of the letter 'o'.

Round 1: WhcFDjEQm9

Round 2: 4TWSDjtAeb

Round 3: jHfk4ykZBC

Round 4: 86BNnSn7Jp

Round 5: djawp7Tw6W

Round 6: hcdLwUKPTC

Round 7: zxEjEhCsVP

(Round 7 is a bonus round that we do not cover in this workshop, but I felt it appropriate to include the password anyway.)
