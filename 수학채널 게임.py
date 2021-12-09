import random as rand

turnDict = {0 : 'A', 1 : 'B'} # 0 : A, 1 : B
turn = 0

num = 1
nummax = rand.randint(10, 10000)

wrong = 0

print("\n\n*** I recommend you to play in a full screen ***\n\n")

print(f"The given number is '{nummax}'. Do not make it!")
while num < nummax :
    command = input(f"{turnDict[turn]}, input s to +1 or m to x2 : ")
    if command == 's' :
        num += 1
        print(f"conducted +1, now num is '{num}'\n")
    elif command == 'm' :
        num *= 2
        print(f"conducted x2, now num is '{num}'\n")
    else :
        print("you gave me something wrong, input s to +1 or m to x2 again\n")
        wrong += 1
        if wrong >= 3 :
            print("Jesus f**k, Quit Turkey your trolling. You loser, B**h")
            print("""                                                                                                B::;;;;;;;;;;;;::.QB                                    
                                                                                               BE.,:::::::::::::.,B                                     
                                                                                              BR,;;;;;;;;;;;;;;::BL                                     
                                                                                            2BL,;;;;;;;;;;;;;;::Bs                                      
                                                                                          :BQ::;;;;;;;;;;;;;;;,QB                                       
                                                                                        :BB;,:;;;;;::::::::::.;B                                        
                                                                                       BB;,:;;;;;;:7cr;:::::,rBc                                        
                                                                                      BQ.:;;;;;;;;rEQQQQQQDgBB:                                         
                                                                                     rB,:;;;;;;;;;::::;;:.aBJ                                           
                                            BBBBRMMDPwr.                             BG,:;;;;;;;;;;;:::.:BR                                             
                                          .Bgcrr77cs1XGgGU,                          BL:;;;;::::::::::.KB,                     KBBBQQMZs.               
                                          cBBBv:;rrrrrr7sHgH:                        B;:;;;:rs7;;;;:;;BB                   cZBBS;:::;;7SOQgHr.          
                                           vBBHOHvrrr77rrrvSRa                      7B,:;;;;XMRQQBQQgBB                 rBBPv;,:;;;;;;::::rsaDMMREJrrrr 
                                             ;7rZZ7rrr777rrrsgX                     UB,:;;;;:::::;::,B                5BMr,:::::;;;;;;;;;;;::::;;7JaaSHK
                                                 :gEr77777rr;GB                     Dg,;;;;;;;:::::.5B              JBD:,:;;;:;:;;;;;;;;;;;;;;;;;::::::,
                                                 7Bvi77777r;rB:                     BU:;;;;;;;;;;;:,Br           rBBZ::;;;;;:LBv:;;;;;;;;;;;;;;;;;;;;;;:
                                                BBi;r77777riBX                      Br:;;;;;;;;;;;:;B          UBRr,:;;;;;;;:rBE,:;;;;;;;;;;;;;;;;;;;;;:
                                             ,6Bp:rr77777riwB                      .B::;;;;;;;;;;;:cB        RB6:::;;;;;;;;;::XBr,;;;;;;;;;;;;;;;;;;;;;:
                 .2DQBQMBQP;             7RBBR6r;rr77777rr;KB                      .B;:;;;;;;;;;;;:vB;.:::LBBJ,:;;;;;;;;;;;;;:;BO:,:::;;;;;;;;;;;;;;;;;:
                BBJrcLLccc5RBR7        BBR1rrirrr777777rr;JB,                      cB::;;;::::::::,;BB5P66S;,:;;;;;;;;;;;;;;;;:sBZ;,;r;::::;;;;;;;;;;;;:
            La7BB:pBBRDg1::;rJMBr    ;BU;;rrrr77777777rr:6B                        BX,;:::::rswwwSs;5;,::::;;;;;;;;;;;;;;;;;;;:,:6BBQZMgEasr;;:::;;;;;;:
          BBP77GBB6r,.:7rr;;ii;1BZ   B1;rr777777777777r:BB                         B:::iEQBBBROEGGL:::;;;;;;:::::;;;;;;;;;;;:,:LRBG     ,rUOgRDpwvi::::,
         B7:UZPBX  ,cDBMMBBBP;rrrEB:BB:r7777777777777rrBB                         BP,;:rL7r:,,,,,::;;;;;;;;:i5s;:::;;;;;::,:rgBD                :L5ZgRgP
        aBZBg12BLJBBBBZOMBBKi;;ir;JBBr:r7777777777777r7pS1,                    ;7BQ.:;;;:::::;;;;;;;;;;;;;;:7pQBpr::::::.:UEX.                 ..,    . 
        QBP,,.sBBBBBBBBBGBB;:rJr:;;SBKi;r7777777777777r;7aRBE             iSRBRBBX.:;;;;;;;;;;;;;;;;;;;;;;;;:::7EBZr:,,;MBBv  .:;c2XERBMBBBQgOZKaXBL    
        BU:J;.vBBBBvBBBBBBg:;cRRG1;:JBgrr77777777777777rrrr7EBw        BBBD2;LBB:.:;;;;;;;;;;;;;;;;;;;;;;;;;;;::,7GBgGBBRrrsX6PKaUsc7i;:::::::::::cQU   
       rBBBBRGUBBB   BBBBs:;,7BBBP;i:2BX;rrrrrrrrrrrrrrrrrrr;7ZR7    BBS;;::BBL.::;;;;;;;;;;;;;;;;;;;;;;;;;;:::;:::isw7,.,:::::::::::;;:::;;;;;;;;:;URR:
       BBBBBBBRaBB2UBBgJ,,,:2BBPBg;rr72rircv7rr;;;;;;;;;;;;::rcSBB5gBK;ir:7BQ,.:;;;;;;;;;;;;;;;;;;;;;;;;;;;:ra::;;::::::;;;;;;;;;;;;;;:r5r:;;;;;;;;:::75
       BBB BBBBOQQBBBBEXPc5QBBXBBi;rrr;rr6BBBBQRGXaEOOGZpKXGBBQggBQ1;rrr:7BU :;;;;;:::::;;;;;;;;;;;;;;;;;;;:PBr:;;;;;;;;;;;;;;;;;;;;;;:7Bg::;;;;;;;;;;;,
        BS BBBBBB:,:::::JBBBGcBQ:;r7777rr7rrrrcJpMR6XaXKpGDGL;;;;:;irrr:rBp.:;;;;;:cpas;::::;;;;;;;;;;;;;;;,cBc:;;;;;;;;;;;;;;;;;;;;;;;:7BD::;;;;;;;;;;:
         EBBBr1Br::,,i5QBBZicBZ,;r7777777rrrrri;;;:;;;;;;;;;;rrrrrrrr;:5BP.:;;;;;;;1XPMBZsi:,:::;;;;;;;;;;;:;BS,:;;;;;;;;;;;;;;;;;;;;;;:,7BZ::;;;;;;;;;:
          PBr.::.:vXBBBBK7LQBc,;r77777777777777rrrrrrrrrrrrr7777rrr;:1BBr.:;;;;;;;;::,:7agBRpw7::::;;;;;;;;::RM::;;;;;;;;;;;;;;;;;;;;;;;:.LBs,:;;;;;;;;:
          JBB2775BBBBXvvXBBJ:,rJrr7777777777777777777777777777rrr:;pBBs.,:;;;;;;;;;;;;::,:;cSOQQGJ::::;;;;;;:sBJ,:;;;;;;;;;;;;;;;;;;;;::...RBv:::;;;;;;:
           sBBBBBBE2cSQBGr:::2B1r77777777777777777777777777rrr;:iZBQr.,:;;;;;;;;;;;;;;;;;;::,,:r5QQXr:::;;;;::OB;:;;;;;;;;;;;;;;;;;;;;;aBBEE1sOKc;::;;;:
             UBBBOGRRP7::ir;;BG:r777777777777777777777777rr;:7PBBQi.::;;;;;;;;;;;;;;;;;;;;;;;:,,,:LDB6r:::;;;:rBO::;;;;;;;;;;:::;;;;;;;aBBg;   ,JZOJ;:::
               sBBar:::;i;;rUBZ:r77777777777777777777777r;;XBBDs:.::;;;;;;;;;;;;;;;;;;;;;;;;;:XZ::::7ZBEr::;;:,sBL,:;;;;;;;::.sO:;;;;;::,,:7p6r    JRZ7,
                 :2gBgpPZQBBUMBrirri;rrrr77777777777777r:sBQL,.,:;;;;;;;;;;;;;;;;;;;;;;;;;;;::gB;::::,rDBs::;;::DB7,::;;;:,:7RBJ:;;;;;;;::,1;i2ED1.  :gp
                     :7LL:    MRiirSUr:;;irrrrrr777777r:7BU ,:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:7BX::;;:,:XBa::;;::ZBp7::;:iDBRX:,;;;;;;;:,.BB::::;sgO   B
                               BR7r6BBE5s7rrr7r;irrrrr;rBS.:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:,1B7:;;;;:,2B2:;;;::rPBE:,:BBP;.,:;;;;;;:.rBB,:;;;;::BX   
                                SB2:rspgBBBBBBQwri;;;;:BB :;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;B1,;;;;;::PB1:;;;:..rK6BBS .ZMPL;::::,:BBs.:;;;;;::QX   
                                 :BOr::;;rrrr7pQBQRGXJJBs,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:.rBr:;;;;;;::s;:::,;UBBw;       rOQpc;,cBZ.,:;;;;;;;:SB   
                                   pBOJr;irrr;;irLwKZZBB;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::.:BE,:;;;;;;;:::,:2BB5              7ZDMBO ::;;;;;;;;:7B   
                                     7MBX7rrrrrrr;;;:,wB::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::,,,:ZBa.:;;;;;;;;:,:RB6                     :RJ:;;;;;;;;;::QJ  
                                       .pBEvrrrrrrrrr:MB,:;;;;;;;;;:::;;;;;;;;;;;;::::,,;wEQBR:.:;;;;;;;:,rBBL                        :Br:;;;;;;;;;:UB  
                                          XBg17rrrr;::BU,;;;;;;;;;:,:,,,,,,::::,,..,:JDBBg5v:.::;;:::::;2BB;                           DP:;;;;;;;;;:iB: 
                                            LRBBBBgU7BB,:;;;;;;;;:;BBp5JLc7i;;;vwKZGD6v:.  ..,,:::rwEQBBp                              sB:;;;;;;;;;::OG 
                                                   ;BB5.:;;;;;;;:.DBUERQBBBBBBBBBBBEUL777vcc7L2ZBBRU:                                  1B::;;;;;;;;;:;B,
                                                  pBOB;:;;;;;;;;:,BQrccccLLsssLccsUPEgRQBBBBBBK                                        LB::;;;;;;;;;,;B 
                                                 BRiBD.;;;;;;;;;,7B2cssLssJJJJsssLLLLLLLLLLcLPG;                                        Bv:;;;;;;;;:7B  
                                                BB:HB..::::::::,,BR;7c1HJvvcccccccvvvvvvvcvv7rJRBa                                      Up,:::::::,;B   """)
            input("press Enter to quit game")
            quit()
        continue
    wrong = 0
    turn = (turn + 1) % 2
print(f"Game is over for {turnDict[(turn + 1) % 2]} to overflow the given number '{num}'.\nThe winner is {turnDict[turn]}!")
print("""                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                           L                                          
                                     Jr   BB;   M                                     
                                    :BB   61H  5BB                                    
                                     :,    .    ;                                     
                                           :    .                                     
                                           ,    ,                                     
                                     .     :    :                                     
                                           ,                                          
                             :L1HEMBB .BBB. HBBM ;BBR6UJr.                            
                          BBBBBBBBBBBBBBBBL,BBBBBBBBBBBBBBBBv                         
                          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                         
                          BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                         
                          BP .BBBBBBBBBBBBBBBBBBBBBBBBBBR .BK                         
                               BBB7   .BBBBBBBBE    OBBB                              
                                         JORZr                                        
                      iBBB,                                 5BBg,                     
                    QBRB5B2    7:                     v:    BgBBBB:                   
                    BBBRBBBBBBKBBJaJL7vvr:BBc;r77LJ2XJBBZBBBBBRQBBB                   
                    BBBBBBBBBBBXaBBBBBBBBB5gDBBBBBBBBBaKBBBBBBBBBBB                   
                   ,BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                   
                   ,BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                   
                    BBLvBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB6rHBB                   
                    ;     XBBBBBU    ,RBBBBBBBBBJ    ,DBBBBBL    ..                   
                            .:          :XgDOL.         .:                            
                                                                                      
                  ,:                                              .:.                 
              .r;;c1,                   ...   ...                 ;L7ri;              
              :s:,::r:,.                                      ..:rr:,:rJ              
                ,rrrrrrrr;;;::,,,.......          .....,:::::;rrr;r7r;.               
                     .:;rr7L7vvL77r77rrrrrrrrrrrr77777LLLLL77ri::.                    
                                ....,:::::::::::::,,..                                
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
                                                                                      
r                                                                                     """)
input("press Enter to quit game...")