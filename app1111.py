"""Jupiter Digital — single-file demo deployment for Render.
No real payments, credits, or transfers are performed.
"""
from __future__ import annotations
import pathlib as _asset_pathlib, base64 as _asset_base64, zlib as _asset_zlib

# Static demo assets are embedded in this file to simplify initial GitHub upload.
# Files are extracted into the ephemeral application directory at startup.
_INLINE_STATIC_ASSETS = {
  'app.css': (
    'c-pmG>5t>cb^q?ag4xDmS`Mk<eMs0vY{Lc&#7F?cK=QFj7F*0vqC!&L(-'
    '!)F&#Q~9i)v}?V0LCjvW{0(uipE;qiQ$w{dD!b6MB8$J^5vjMgHFNYBYS?Jq3PHM=?B>FT1BEX|kq-hw(BrsKW53X_iM1brZbG8${oh-33a-'
    'VVdBYKYC-'
    '|KoMMEOp8nyb<js#G<m`wMUfQR3E>?&mU!4b)hI7wUp(_d(0fp0TJbwP23eRyjJ$I9l%`pnlc(cl!u9T{KqxN@c<$O0(1jCRHW54ysBSOgF38W'
    '{N!0_Y`?sC%1mXF+6Q%Ia@KU1ZAa~=)&2o3^C&}jHH^04>{daF{|K6Tnc4a@*Koq?BI84XRE&KZYdPKuZd)oQ?V|(%rxP3WHyTJE<-'
    'Z%Ye@)~q(yZ7CnPZJ*8zo665pRwzq^SOgbdLJizbbk+oe)|im{z@PJ1hw3s{)%6E?ELM|Ke@jfTGY8CI*s0lhql>Qeb*1WS2R4c`Pl4BRDF9H`'
    'pc>2ugjMW>mBIEyC5bbe#7Or7U-d`kH85BG9q-Ep!pV!xc(?F)6}2b_H@2X?ua{FO)lvG4H#WXy<K}c00|Q>d95zP2&A0*mW=KLT^VV-'
    ')SlG!YFzaLn%e%fJM|~btL~b<x{TgyJGNzqU8Frz60~=WAnm0fPknvuFB4t-2v&9MyS8?o%B)I&75NvhZ<-'
    'NLJ6QXVL*O1l_Yk?~c`4_2*A7n;VZ$@3$aHyIKThxwzF(L5tvYl(KZn`*yBoc}xe+kfW>0$&+^`Lzk3%R`2@_ZnwMh5@-'
    'ARj<8zrKT^HqJ5BnmgccG!Gu+X|NEt*xg6YebYLzw359cjz6Kh&I%8`1_vx1N*>t&}HiP<23Z&u*d6f3)Y@9zP^Yy32V!2F4`=+zWT<BZ^xr3o'
    'k$eGZ~na#t%cF@o&4tCzjyq56fWP%?~m=Ft?^a#Nm%M%+T*z&Cg9|c?KpV-se8Yk`>~}whe}v~kPCZGjzkUo>|gQFbRY(x(HfujRo9+(1F+e%@'
    '6taY0Jfy3@i2Eu=S<z|uZR8rT*j$w-'
    'aR0G!mv{+Ot!=xw${tZYhhcD;uWdy)h+3T5D4pcIiB_}=)4O+2wB#X_3w54OE2+9LJAw)8Kn5AG(luNmj!Q(-'
    'op2lHXW#ay2^Ek0EdBp{jKx6%XDyl`}H?lV2y(}Rs+VTt1)&lGcQA1@5w(PmX7dd!X6tP2;HrpH-'
    'ob+!e)@g6_M;8taYFQcUSqFkEn)Xq`e(r7Wc{`=yOh{0edB$-hj-Nc|N1MCQ}u|Zg5~E&nfKK!Y4a+=9vKl?d>bp*+V9DSK_80@KyBv(@*;~o='
    'Zc2;X3v((BEE2AEy4i%gGO>T?k`xp+yx^m?W<FyA9$EFDBGk0y~guD51~DAJUwqwjbmhmz4;zl_FtCW`YWI55L0DMkcq}*vkQ(>Z{C7dE!f|hH'
    'ht#E1Af&Oz+>l_EdxH2|l*8U9UvLDE7THXY{vCa>=`kE;l~abSDvo$7H!Ta7KkUu$og_0rH^rc1Kv$4(})EdW5w+?#6HU?b!>$8oz90lAQ9Y$T'
    '+^P*}P<8EeMhze_?`UCI>Y+z(oFm@UhzN?gVpM9onvb4mMY@si>G+DHhJf2=A;Gi<V*qAye8_Nt37ZraPkcbiJ`MFpJ;0E=V%kA=wjT1!Pr4xt'
    'J*XWiBu0Gaf2{6$Up1gc)=WGQ^K{y~)y&;h0i&p=;ZbM!7tDD#|iZ2J2WfH&NJbybVDTqzRD(90rgXhLu!Ru3wl^*C&ub>BGTC-'
    'p%yhVc0>#5p{b(RDdd#sI#CKp|Y&7jNLNI%3=}XoGt>bIkg=gRkcL5h`%sD5iJqXz;t)K4e*)#BR9arzYvS0vO{&YA&j1)AP$m7V|m&eC%!^;h'
    'BKLXqP*p$&Jv&Z-2ec^gBW%m7D*Z35)oRfycN2+XX0a7P8b4$t6#gK=IvEzsJQ?lx`DtOum*^BkP0|k{Eo|^f0MUBps8-'
    'g#5$WBdm)?|hqkO>#3-5<l7csf*(y@`Uj<?Xiv&>haTn(E_ZlDjWm#iQ2sB|s(6G74IK)L`EOI2)aamS%SEPam;wXu-K<2-'
    '2p&3NN*q;`jy#*KmEx=zZN0ZU0EjrvFna3O2IGC*rA$()wVk*IyYUpq?=`h7&cUgH-C24mcg6Yb;69S+H!x^a^WDU$a1zrD+-'
    'oZ+tuxmWvuDfTt!X##R21Es5SD3ktfl&eV0dxjcu?T$F3e~rFia`9mg6RyCk^xDv)AKsUiMrQr<1NCO4p}&dN;I*rBcH3V>u39xFoHif=hJ4KX'
    'pue)A8JVCv;D^eHzmLsK|*($qBr*I0<WL)x~R%T>M_^kF5w86HQ1?VG9wFf604M8eWy^j)njTj)zzpk)aX+hWvD=Gy}ctoT{ISgsZ0cQWRmZid'
    '@2Ow4dyVZqHd&M*?0;DqC+|(f`bH=C@J$glqW!6vJ{p~-'
    '<6UPO50?N45(sU#^We9a3R@zg*<GrH>GVDWMLjhGD|JRx2PgINhu$uQJobE3rb+TJ&kyBA}YF{GF%{{^%o*5Xk!u*oD6P9EpWO0D2~%q82L}Q1'
    'i9TTdkPxPR2B-16-'
    'mj6`NrpJ;wo_|=@D#d+?|>76Z!`D!^y>Nl_(<86B>FUt;1SA2aykO*?kJ*C`(KCDJY{LK^q%<sA8ODI={p+Q&C!HTKFpRv6o3jk=*iGN9FP&h+'
    '$9!=V<Mo?TVYah-y(+s8lA|rCyn)F~<j-'
    '6PCeko@c~~@fKu$%@r%mB~>sK?DJ(4d~7cxR0Ubz3ME5T<U$v)Xr3hdd$xEXF9zWNHh)x;ur3LFdqorI5N@WWl9`sShy#hA>k6l{Dt!XNLX@cf'
    '1Na3-yy`L0%}wI4Vn*pact_Bs?4A&|4-&mW-'
    'x=Ycr4I3RonEdQvRUUU`Y#p11kw{EEkW~u!cX0!M8((q60~`H9@|kNg5YnpPdj_&c~O_u{|^zIs|{Hs0853Ms*qQbO#dS21=CQiLTyTgWq>0I?'
    'BINohbmK;PKZ340h-u_b`S@R)I)#vnzjQ*f!VtZ&twfZ5>SZZAFv8kR}xi!#3-@@Cjn+c7-}_Kj-'
    '}2~Viq%^^7PHj>wq{j04AL|4^cq1X6e~%;SSW4SND^$888Bb84Fs%B+s*Go~GO`ia^4AB8*@=8g!+fkY(|maZj1#Co^cFjxJgCqB74bm_63Y46'
    'h;@&ml-N^A+1UNb|*z*fDoEaBE+J8B9@<S57Czv&?uIKr|vPUmtKj%EK2<DeCjr?6rBrh)#%qf>W4L-IW_96!jG=L(F`iX)9WCopTD|5*QCdd-'
    '_K9sIX~QjMxRC>X_32rZE81H5dy}1fQ>x2i~wV*v?iwFw`pg+n=dLBrnmLEAXbJKaXEBk7BF2D64OaxoB~j+-'
    'ER~trPpYO>GhF2F8U6;J9^}UiypJga7^P1=LvqrMBmxg=u`h-'
    'ZbSn#+AxjP%(uNIV(kY!fcXpiqRyE3|rc(6Thxl5gw4!EabWYoS+yGOalwxkN_+WSOX+NY}U?*6GN7Mm_p|Tc$9U_>Nl6JyUKuyyqwz8`z%p1j'
    ')Y{EiA-Uc8={h}7O*QSJ6vCTvPGu%-4*~ni=3W%V%vaH#<k>!W}=6}abp4=aB8qG>|rCDB|Nx9A2zI`EsS*@FZ0-'
    'p%#in{cIxo;pP)cvL;NvwOzFr`gP^Hd;C$8HF5{&nB$|;knh>D8r*GiPD<W)68-'
    'folg8!c`M?AFEZbIdy0}}_HVY^j__I$6v;dZr*hKTsKu!$lmf+lWekeUXWpJ$KCTt6ay3_>d`<hy-)(o~AsgA-'
    '?IR295Vh0g7SI<wxKr!m(9C0b?)ug3zfX0;`CW3Gqlv<O9i>oP<mGE9T2gaw|^bQvF6hScWoEasI-'
    '#g2Xy?#$uHrv!vzR$D~2Aorhxa`FsNV<Fny*8K_Vs4j1U8Px&rB#ly9kfGQ`X_@6{E_NRJmjREX+Hl=OlE5s|v@DDow#Jh<tMNj^8Q>2APnvQ}'
    'a51w+kv37FSFkmWQ{>0xQWAjyQ|m4Jcvcf-ois#mDdnvVCt02`obex^tX^CEM$yIr54{?aE`vM@HGhv10@U<Gn1qr<ps<wM$&bd&XA?xX?Tnbo'
    '2c>$48WvyCm@kf{z$$w%8PJSm6GO)fV<~nWgzF*eAWmEm6kyB+?l#OeW`H_NSEJ7&Kpn3Is8{0CWYpel4BQve%sE^hdNuUIGkSnXH{9lHIX(I8'
    'W@16#KyHmh0EOL$$^f>K5f9{Lm*5}PgMX0`XvuU7BA)xC*mwmoNx)Aky?`&f(@I5ENs(4LQb8V_bObu!rfoFG<}K3tW?BI8O<03+Q9@HTR^ZVr'
    '&-H{FhQep$PDA4|YlhTz3<cw{B%p0jY$S9x^dL>}v&Yi}W)g|t?MF>S+0kYAeX=-@h&O-k=~wQzT5}rFkiY5yWg$Cz+*$~83L>wvW>VFG-'
    '()snXBd~UDW$YdoOaIgP_<o>g8B+9y%-'
    'IsDG_sPx5`BuRpu8krkFVsWmco1Y1u_Cg~K)9s*JrkQ?U}EJ};l7D%t&gC8+*fr%X64g~kuSmWiMco&dbw6<Qte8Kdbrc9n49W>GP!@y(lFtb;'
    '(+a6v>-JS$~xf`@GdtM6<<^?HD4?pX@?P?w)D)Qr%#Pl1iaqW{bfJtMy?Al57ES7Ag)A;!RI(Tt)|QRcp-iReZXfNf%&&ED)R$5Cc!BECfhreS'
    '|EkTg%Lbe=%TCR)UZJ^xiTNJ3wU&S$#PntPx-%g*ctLRpzA?TBq(U#e;Jh;QnC=8mk)otn(e+h<C~4C>SsPMS(q63p=}&uK&X>C^1Ny=-'
    '1PVXWcAFf`4PR2L)G7`r+M6Zoy>!Y00)n=8RNlFGcAf*2*X6hw{+Gm+5fWfb??fSOFL&GZDxOl=y?rxWA4ZnWB_0ZMjBh$F2sm>Y4etu_n1Xoj'
    '}o%#2o()t-'
    '_JO!Z1@RB>NKlE1ky`OR=;aAhPR)G(KKff9jy)Ec$~<tZ;KA$^j$cq4y{_#X6tyih~{Qj$c1*^HJEcMZdTV1y0R$F@e}q3nq^<H6{=ETL3R2g='
    'BlOvI-'
    '~Q`)ZcMq?iR8coQfpXH48g&{h09`R26Fvhb)uF`@|{?eW^9h8(RmI3jj861ATp21PXC@kZ<f?zfegiNv!Yi27%bcF!w)Wno{5z3}BD%2;0oPcq'
    'r!Q$j?il!vGMm-~<R33I68YiZ=OhSFJ$TXm+xM9+Hq5>S^I59|M6#*|?mk1^*k-'
    'k=Xy3P@{nUPef=1vNT`@zyd+Uea)t_hUymJ}OWDAdAae1pu@fVgj0>FC2=IuY?1RI#8N4F^O`Jqt2F^Xpg+t1F}%i58lGPz_RZ=!T$`)qakWGW'
    'poTj-M8XJJCf>sO99TAS_GrxF~r=o++Y4_LzT<PnmQKhW-`?cUEQ<7L9yjRZ(cXIRCP&(MC?h67eAYCwjpnbstTA-;u!gy^&kpJ)T-'
    'JcSnqd>fkjk?rMvhLuim$h*77FTFs%ytHf-xXuqWtn^e0mh<PSRMfyvuW{83^{@Ah;WLtiOY&)MJv*4>5@Re^w&en5`!z{{TtOW0(d7Y`CpQRb'
    ';hBBx)4Mx?S6i|~fg2SR~(!n!9zj#uQnrRWIJS^%aG5uUbqVm|&$1)E}W+q`PFjxtTi319n&nNldq+Agw69faOu#Q8$_6TgZyA0j)PejD-'
    '==0a{_2pl`A3OKw=nwGIfuE=GmoJBDI`6)IeS3S`zD3)9c=;OozE28&ap+9`@+FABIE(=Ho47=O-'
    '+%w*3mH`y!+&3#rtP|4z7RsbIPBQiFJFERqbz{g$i*v<HyD2TIr<}zaYoa@sek!$Or63>$saHM@|Arf6u_^aWXF!j5Iu~S|B}Bg{7)!lM>&OGi'
    'F5ZL9UWtv#t_%p{LSf5iMth91>*_|WahK8nk;=(wq|lo+whVe>GuIsCS0@A<@UDIVZiwMkWHl2Z~Dt{eaK$`)dAmlJUDl?xh3TSzp8;fGZ%sni'
    'BvhXQa%UU$A%S8@}+C5o?C<r!J3#z83ZU{HhZ%wFN#Wcx@h_AWXlb&ZG}gGCq4ZCA>)(gUkgD$H>J0<t_~;^Sdof~_#|QSV6Ue6t5ZUKC<+F%g'
    '$z^*xwyf#F6A(awYYi{Hz_4e6MTe7lHm&<9hwHK_raAAs>puz%&Zd~nrXFfU=mw#TXMG;6e===ZnFa*Or0JO)0NlJRQ-EcL)kk{l#&&vOP||OA'
    'Z?y(hQ;qjx77b$dV==J8CY8~THpspaEW_9L|y9XF#NOZ8%Z2e<6TuyMu|0hm1PMm_2hG;B$UzAnUM}5m%fd*q7{cVaXxXJmotl6Zc~=Qd4s|#S'
    '|NcR+@H4%P4Fm|ud=V{K~H`OmLB1q1>(!uzW%C3$J~;c-TO(<E)4<9<SD7Ew=x)vY(0Uas;Ek0tMNE@0{E4>X0$BN#mgt!N+~AOOj)BLOS-Lu#'
    'e*=6qgqs=o<cPhnPy8H$rJ1jiqE|Ba<i(}#WzKNV$A>_-`c4<7@V<oSR#-'
    '@Fo{UyTUp(>OzJEqxe>Vfwki<`IBj~bM5mK(Y5OaOxj;SS)O%@Y1Vv+*`ba`OQJSPEy?y#CQE20agJe#g`ibbhTWTt>9yx5nx>oa!i6ShUbU8|'
    'y*74`M{0vByI34UcBt~=~Uyg~}DJ7FcwZPo4b}nG`?2D57FPTnRmZwGe$=OLWlgOmNa!N%>oePUNMu8Ug<cB?oyE|@RHETSfw)5%%y%AvrO)c7'
    '{X}{xoPj$LFOzJ95+#qwK)ZNCL*%z4m`@6!!TEDtmcdx~OY4m=h9$Qmff$|_d=J0oxWA7rkn=Aogl8)<yR9Et${{t~yhT&E+-'
    '&jm@>4c;oSkA2Q0#(<K*veW$ZQOSn<BlNL+^4|x_Xa-s5mmiDafoZ;R69&cVLxB^2cnqz0a3k;U+eZ&Idb>VdC<UY@D_$F5)_nyE{4=`r?w_-'
    '8gVYwwc})QE{0kWI?^ADHiw#Zo3li9U+Y1SIcHI>p3I|0ww~S06&lSdxZ49J$;U?)tT2_U>6}~W`Na76*iP*cD}*o8FCBwqt}{82kiF32hoL|M'
    '>?EM?umA?{g1LuHPoCOGVhm7gVKv=QI{sLEnr@h;c?9&DPCrV8N68?fAU689onsQlK!B>U{LJ^>kYgA?`S5-'
    'h!pgN2{D+Tw8~kCI3JXP!xZ3I|PSU(?Y)+uLES-qelT;<SoQ#(zXO}E1Z}DKDv@Ea&gviBd&CQbuvDJfa_iiOo7M7(%nD7!CtRPgsNN4x;7!P%'
    'Vvxud0o}J+$hRJd&%{(GGNAkY($dF`5=0XSLmgGn|z@90QR6>QGD@~F#{HD<gStHbGlVZJ~Js9oRS~*8MYV(v7Swv=DDWqIe5=&V*^x(L-'
    '2|}qtE`yje8&fTlS&r(ZU``@y9-&GnJwE=@y`K-'
    ')Pf^2KP4y^tDrX$fhxtrIWJ$3L0)7<_KH;XF#(y{gM9yvs7+m3PYlk2BTjdC{?41(PdFk@9T&}m~?39ebrLg5h!-'
    'UT^^?%zxyLcT#?ZS*)G<wx?AMY2Lk$J$0HL2kuZdfS_AP&;FPCiR4u(^Y22fDA%qS<LV{aiN{M1P_e&5*Fh3!a!HI`%c{JaKq*&9a#@8A8*_$='
    '#rEW3V2QWb=bJ&MZcU&m+&OjIrjkW^<@(v4VVGKJOZ4Mow$Ok3urDCw0TXjSF`hZg{WE>-'
    'PYFG));PCb2ZBrc|?iC4ChJv+hhrQmTr9@wlBMT^bls@G$jgR7G!)gjt;4$keCGPtE2q=8oE8OCoyahM7xq+LMi*s%FAZA&VoLM)E{S^yn3=8p'
    'lb8L3th({W&ur!58GFzRTntuea~i$nye~={$pU2mIjxhA88FatB0pkn^<{T+0zMeDv(dH&qKf%r>{8YDUAl$pP>r2}LOwcr~X+<hK0I!shfcoZ'
    'hT862`pB7h2x9?xJ9~UBoyGn%I5HGZZz=#?qNQAT32y>h<%U!mP}T(tXMr9G1;yrP=7wW^s-3q;Q{_ye^8GUH14FdJ>xO$-f<O-'
    'J)md=yXW)?XUboqLn*{sH9QUu6a6}xmd_<OB1$n>D2(saeW3vgd^ag$fzZ`Y}I$L99?jXQwCw4=n<Z~f;v=^f0(mZq<r%9>zCN}x18hsFTg&2^'
    '7BT{R+x)9+i(;BB#Bj##hpiy#mhC{0<-PU_;j`Q>XTB+om2c$*R@mfxATuQUlq-RK<iRn%hJ*BjbH$t+=xJ|s{7pV;e8898Nwb~1Cy-'
    '!Q0_my(S&r7sbYG_r$VFU20!yc!YEWf>Sz7c+w;`B3RZ5!b3*;fK<#XU8S1|2aU*|iTuyIS04_Inyf`24B))aWGaBYQE7U<r7htGImTuhBV0vM'
    '1+_@XuZeUQ8;LQsa<m2MnH+Bq5oGPKl?&@?dsErtP^u{uYZG79wG-hTP$FBG++?1LtSL(5}PxG7yvs$D~r7)1rc^HQUBJB`}?o5#r`Q62$Tb~;'
    'dh|+TOWr~=b)>5h$j%1UvB)Pao!i;-'
    'o3XC#!!9!cd7RnDY)yTWqscKu_!%UH3%BwOaz01@W`;VqDIwAv2pItR#quMlUGH&^3h|0*<gq1Bze?}FKd3OPwT8ng|ARMIAr(5JfhH>v%Mj`Z'
    '^<pvGO&n+L{lmv?ygmWH9I+W1fE^o`#1&=G%$|WtiQpDSpZI9KP(`{;Bm*u{=mO?!bbEk@>+)Ohs3`fEZ-OFqkAcQay%nx>Ga`#Bmis%!t&fpN'
    'TMyEeHCp6If2&${c?Q)H#OQpOk#^f4c(UnKx(t*12F$4KZtKZxUH5Z6T&M<5=czgqCKiocP?}l3bq4s_dhyU>Y(?|1vRU>>K'
  ),
  'app.js': (
    'c-pmnYj+#RmEd>(iZ-ICfv^Drd`J{1kSj}ati*amls%qsc%&xKBw&I7+yE#t5YDlr#CBF*zhbX7j$g8OC%Y$`9a<JGSP$x)`32x#$S>LZsH(2&'
    '2S`r5ld*{IuIH^=_ujg%8vlj$t8S~-@qFt{ZMD{M>(<}j{McIQHp-n^vjLAUOuS$%TsoDrE;KE--'
    '08xrmb<m?H9Bpp>04#rtJFGH#Vgm^P@$c(elh-BI-M!a_3Uojv)UcMR_@rd&z0e0$2w9<w;jLP?360aau-'
    '{HlK7l^qwD!w3trtTcba~>opG!qv4t0Nxm>iusd^piEXi)J{PU%=3#CQ-'
    '(y4#89sBgDOXsefdKrG5JAdio<tuhj?%dhS3#Hz|l~b3m6niV1#R+G*)~>F3YsEqy|IcZ5s-9mgOyfh}`Q_z{|8(UgDp|-'
    ')tFkkCQ7YSaE?vIJ<y5I-TB#Xs@9c#uXD?s6d~V?^mDQS@(h76ueL3jMXMcI_;sqGCJ^XMu*n4OAXt*<cWEXoCcdHFUb$qwu6({?SJ^T#5-'
    'x_WYf0SRR#Mk4wY5u;u_vUbC?|u1wI?vx{aufLdli_{%zB_z2+?FMdi4p~EL;$}luPhM6hhISP`@?N$66$|B{9!m4K7bMI?A@}cp~vv;*4`cb`'
    'W3u*F#I0IaEmHEf?nYDM;5%@-'
    'MdL6$G1E9_KV@RMQ@%!*&l{a`R$)%Wo!7zg2CRw&i3BskDpTgoxL{!Mmtc0TK@_rG*HbyrH&tq&k8TjTs%#axeKrFLy;f%Zerb!;pg{M1HfjDT'
    'f>Jq(O~3XiP?Qf1Kb_%STJFjBXmXMfY%SGs{s%28+Zj{*t?0vV3@by_Z_SS^B+FiyA5-'
    'N(h^)B<1$kZP;2ikSlaht3_460==T6EJ{x{ByoV$F8w?7522-'
    'my%WnOAv*MNT7jE)g%Wrm?<z~H9D%mTwx>vNV8#gTVx$U`rxtgmr%Jpu=Yp3mY$8A*Hdb8n`3U)>|+=gxFm3ZrS{H>mNTe@CrRGQaw)b9e6aaX'
    '-r{<c=KuU>tf$<Ng`f4bW7+MTOc?b$Z;+d0?q*3)Z_-CToy+Bx4_Z*F+}GBfLYovz=o+OvHaXt|ocnh|}jd+ViMUw-'
    'ecay!Mf(j0tQTw9u-Z*=Q*N3>sr4mNPm{IRqE6sxhC-pKTwpg*kKs{pa-covuI!~bQ{YWDE5S?U4B^NZAY#dGWJ;^Gpt0fegEq2Ddn?=(DL{9X'
    'k>L-YPd&AV<p72mxsE5jlHNQym%e9^WY0C}g|re9d03{~yEv)+Vd;3@#zGXJVK-3m;gxB>(4)D~T>Z?&rJQtvs-'
    's<`dya?|xIMf;==)YIB5r6yC>7X5p@R_RnrspBcD>eW`O9s21*i9%|8P8Baq9j-h#kF^ff{=OA#2j)|Ew-Bb`$pm!^GePCTF|Iv<-'
    'L>3K)vA<I=O?Wb)xymA8SBJGLABeeBgBJ3g$ZkVqcC-T+A2&`VQ8Y*YQ4D(%W<+?^UHP5D&x>5QdW73|N5oWiBMlyeFmGGbPLBU`2RfouYmtW-'
    'qM#D+0}Ko4j34j>2&-|r;}%Dz<QctJ)v5e4jP#X!Mfvj%WFDNCaq)DLII%m(&X>X7pAO2zB*N(v?e#Es@db%jRuzE0xB~Em5I<-d>#5sUE-'
    'c<oA5osCAr{aXnqs<jqHSb%#vUQh~_sY&KHhb(=H550sGkb!U<7$+L~rqXD72$xoHJ&pb#C{O6`%WYxWOq7AD-|)^X8bu8=L%C$b<dWGAwd_-_'
    't?bZW+$k*hmx9jj;Q!*n$}^>P75=Bm$F(JIujR<@7@+<?ak3tk3Y!2c$o0KT+D0W7R{fjCsB57SlX0a~1Kwa?Hwj1k9Wi7{r)9&i%B4S>Q#$pA'
    '@SfFw^KIj)0b9s7exTE}DyuJ1Rm>qsPa)Oz+<7T1mbm4$soM6K{T0C)zA;QwSHU@#56%rWbPC0bHw)I!1-+Rue!uTHLKarvkD-'
    '}3;3V;fU$flx#s5DZO!ku7Xwr}Um<8lK!JV8h%fHjWLS*nn9c1B8>6nb~R;0efFM=1#ym^6JB{je_<9{z4NI`itzut0#VEq9C-'
    'galCpQ$XQ{sid3y|ysB`zT=k3{ygr3H1jhLCL_UBzmEr|HIB8p-'
    '!KQGJO$Tr<1LI#i1bKuOj&Do@2~kjLS8HBf2k?3U=YPVQ+BjCuLtj(YOct;rpGC|)0so%J7V@ti``x}{gCj*ZLd<3qg@(T~)qwhLnkWlM3!R?8'
    '9nTMnA2nB-'
    'T^(i51Dz?nG_6(*HZrW5_Kd4oojQ+X|9E{mOaD7Rfu!pt)oR)GLtCZ*`*XTl$k!);mcdv7PiHn}kPaUsTssf@g#N<gbajH7hrhuRgEXQyIR(`4'
    ')hYT@EfDq`t4{$2!%_gy6d0Dhdfh-'
    ';pd^ai0>Oeg!Kxh3PSStKZOVD1ee@rI3vjkjRr{yhtThgU9n;p#OND~A0rJ*VbwUFrJil}TvFI2=0Jr#tn(}gUGX{+SU+_PeDg5_afaLKF04lC'
    '3JimIJ8i8$?S8{>pm*FgGj#}`x<MFIbaz5>|zLJPX*0gND)>vsCZo>crK1Lg-'
    'n#&gggsFQVruzpK7h(mY<H*U8cjBK(<nF<K5K^jvLC1l>K_%Qjd0c9sJZh=e-CA86%tS~^o5=4om~~iF<YhCs)zv7fUcGe)Xq~W5Xi@;QS4J8-'
    'N&ig|EN65edYdrChHE1H6rkKOfH)A$sX8Ff3H()<+&HGV1n>w8cf9tTExf8d<C`kcAtj;L;7<w8BISC?w&6T-'
    '?PR;<Hh_M*?RF`JU#%m(a=o7d{#kRg)mo+EHA*Rv$h_3t$@a#owYgqzK+$Ta(<+XSU%!4mcYQL~^jF6x^7;HYlt@{4)_9=_KqB4&TOHsJ>sT+P'
    '8gQITp}MBI=9N<AuI~empKjKhzI>aNSd*Jkuj;jiS9V*al;7+&D#q*AVQ0(tb4Pl70D*(kjT`(k2fML<5{ESh|H4$~u1QdM?Q&_OG$&7D^YZ`@'
    'IQ+HhZrMwZFCINPm$H|}SDkigF5R<_+C}@QyWX0G!|zG_UGLz}IsCawKU4VgjcyYkQg#X+el~ex*6uI1momW#4gj!KN;jNx$^QGTr?dn|dJXTo'
    'b*|B==Pq>Dmp%W*roZlX(zf5tUVg=Pdh70HZN0nxqVJNvjC5%2V!ofrt#HZnfHgS+LYiAhH!?SF<TIH*u4Z3Nxm|7go%1w=1{^gTCB3vf$~NXo'
    'td`2p!_d-=aq*PNb($~Z`Pvg8+h=?eedvDpWcYaa)PkvAE7IJdFNKU1x8s!nyzO}ez!`W-w}W2rIowml-74A>*$Vbx!^yPK0U42IWjk9QlA%U'
    '--ScZ@yPqlAe}D61J5U_J;w5)>ppMjYwb}Lc&$ULk;{`8b`i67$Y1(5r0#t#-'
    '=#A#>3P8v%^7m0Hq<OpL!il9K%Z|{1K~W&kFgLrn_)}@UmI5_RI|Ci~%~juPw*mh{Q@-M^;)G2i!=C^#HLyTCecZpWC-G-^tFAXI-MWX(wM*%G'
    't=)-'
    'GE>Qy8paM5;EG}ho>uxK(7A{(@)>_c}8m;|x&p++9y)<{frh3lgkg}wKBt!<Y?7NLhDIFOCz0WSYK8)hzGLW0)@E>l7D$V`sl}qQYoV{$FY_G$'
    '4d+x<^7p|N={gU<K#mm;ISFT)yvh+UaTx!da<(AKQD{i;mNeewqdxRD`(~~Nya=k_p#qa}IO<dWpNHh53@QF429I*oM;XdjZ0hk^zqgR{twf1#'
    '))oWN+K#c2JlllCWg>$yEfzp)i_}(gvr>HA{olXszHL1F7$6W`K)F~FGrt^7+iG3Ni)hi2UY-'
    'eS&IFpxprgjk(?($*Dfw@+$wxLhd0O$EpYL-`O4YyJDu1XEF12hmAdgCgLxwhf?TgBs~)vh$xy>_Qo4&JkV-KlgtTgB-'
    'U`6>AAZI)|oub79ql(zsrjn(2Lz6UPv`q)jeFgZO{aHMIVU7W#2oLZyZ72o-Jy#+Mr>W15awoohQ`B&Fne-'
    '!{#n4n%^5kN8#CCbh9by^Bw%zblZyLF^YtxT`(0k>{!l+t6Z90L+5`Y-'
    'TtWfOloen}|l7h5@A3t)TlmA)!Vv@9jELqJ)4fRgl>qos1%8|6|<EdXww+2<@ALCf7L!ADImi+Glq*EkLg@)x=ML<Z)yvU!lg*gwnx`3hEg&Z;'
    '40HtGrF&CFw2H9ewrx;0|n7M2VkJ!HkOm#9HRm{5yyV`S!W2n0oiWC%?h4b=rf11(gE)wRiB3*3~3ld`d(55!!0>*w$%&w0(;!d)9iUf8%1#Km'
    '`jv+#$}6@Dmmh2IKSsjk3N_^oghe=Gb1WPmv~+nsjl;_~YtCFfTB=K9$N@IRO*j!II^#Wg2kQ8W<HPvHOQyffA!xeKI@Vjd(O=%(FW?lcjWCIV'
    '!}0ISAUHpgI8V*=b`VlW$Sy$gNO08tvNbU_$PyUsF@TX$^P0kr3RRRZW58x4AfE<5g~-dkD@VT=p${t5P?Tr7~!EJ-'
    'F|gv}Z*W_P(58n^=kzq;aiMfeNIF1Pr~rX&FP4SqUeR`e`>t9LDsG|IIWi2ET_$~ZJ_r_;R3Gb_r`OX@)n#n7C_V9p_$!+#w3aMkTx<;q1YChZ'
    '`;x8XIqG>_0iu-z?+(;5*D;WYvR3terMJH@!|FZMg2J%Vp!(Fu@hb&A;byb1|uX(ou!0P4YD=jdEeGC#%g9IFTXL@$z&OzpRxx8_?XUbD`-'
    'n~FmnFXX55f_GiIe9_j~!9>1rOmdBh<1^DI3SkOAA?&u{KEphDNe$vct=$H};Wuu(`i5K6IH^wD<lrWbBm3mRv1!=W7NZd2h?8;S2mm7naNhl0'
    '#kEeqmYud1U>2Q#SD%;(ch+B$Cj$w6q7dnpQ_JAds8%V~#tJZpmEyHuUCK@z%NFuSdXt5*TK}5UyxssnL6He$dLYVd9YFpl`yNcC0s?iOTFXwH'
    'xRO6!L;{`vt?hJMl~JFC73+}F?r0-'
    '&U~gVptf5(r08wl?c;3S;9x!fAR_OJeY7I?}TgAm5F#d!Aci{YAM2jk#Z6BkV*8*7V4j<BRP~Pt^ISuHiU1a+#4*V%jOWJ7h84K>ck2O^@Iat<'
    'C$1PWRIEzbtIEeOj6YT<-Q+vScVLGtK(4;CB`&SDWFXUPv&B8eeOXY-'
    'xGi^&ELM>d~DA*Y|KK9rascl%@DB0J{r;^U@SD}v_#NF`H8<`%Dpq)4Zheq3`LtJfT3#!0GiJ8~yMYp}xD5p`g;xt>p_j-La#7c{5r`oKP@O_S'
    'd-'
    '?(A_@+=6i%gxFbzsFx7ilITe>@`;`Jf6e((VbUci|W_B1~&CFLpIY{Bw&EKZYcnLj^Pg6r?x^PL=k5kDDn8ZXEVv`mJ+~^CM$yeEYy9zo9R^j='
    '5-4Xw`YC7>8IK9zcc)9?>6Ez;LH1XjQa!n3fRi9t&O*f$PpPxy$Li9#scqgE>O1JzTWgJ&qIMT-'
    'g*;p`guF1_piu@V0ZX<?_G;<64172X;layZUs)yC2HA2-5vHz@BWLJCvf@orY)`7p_1aQS(e&G=#-'
    'E)QDgIkq9{5)38bjuu6yDGQX@Q8KZ1>eo9)5go7V6n@>tpBQ@5?E;_iEbQZ*gTf3(oE1$OCUE@cA|!x^K;1Z?JA*nzwJ4QUz;xfqOIkwY;I=^%'
    'Bg+i6-'
    'aGDX*Wz6WC@b%7<xr+olQ>No3ZqVxwUG4q0xN5ZC(cop7L_&%fX2A>kprP=M+a?5JY6fuY^NkMb1h#JOzT!Ta=?4w7;PKDRFJrx;A?@y;xf3UT'
    'CeN^%RR1}_p)Pb8a$K)vZnPbg!db2dQnUib`YE9_71i%9;)c&Vhr<&G=J8oyJqem?&5r{bBXo+hBwd}=g7DA~<v|*nKJ<njcW9|K()|Jr6qDB6'
    'W)G~ri-A8(lK0oaFgZK()$!evW(7?bx*l2a|UOIK<^h<*Hz>LSZW~*N7KqWh~IJx9(mJB$7{8}l^RdNKMT7?PHW(-'
    'NtSsXH6{0FD^K<KroChZYs;zy5a4?u7>#m`Jn{wiq&W;b(!-'
    'R4@|b~TMGSLymt)pu^;qR{hY6w^gm!iK)Rce7~OV_IwdOka(Lm@o7XQkMtQ^(vW7epd=UtHO%^Lm~CMWPXC73Mr<PG{RYpOAs4GkgF}TdFW;3U'
    '4x4{YV~4P`yW}(n9+{d*q1IYTnP|Q9W6oN28mW1Gm4*L$e9d?p54+Rh(HFg7x;oMuO8{4ihHb9(FN8nw62JBHz$56*)$Qcq;#5CKzdo}PK;8Z6'
    'daZwBC@6aag><3FV4rymH{e<rN&te_T5IiT3hL)HxGfJYRRR57bWMS7Ih>`%^t7;4Q*&?i$*KCy4P6kQ~^!)UAoRz%VRL$FK69@Q`)L{BOc;bP'
    'ryfY_z!_ddhaQaEaHp`EV3LxSP70<u@Z%lLt;fN5*7qggi|CP+C;abB%6bu>qOryfW&q#Ws{{qA48(^a~ApmlOV6$#w`GsDb=Hlsyt66{In&&('
    '?C!oBOFBil6&2)b*vQ+4=D7xhYsg}{WTN`>^8t4+w^NF2O}lI%1+gDE9f$Yhwb#}V?wWA?AfQAjSjS!y#km8LYUhE63ecy<FB`y0Pu{XS`ux;p'
    '$eE#pXslkYpyYl3rs|_&)z%0<G*A2`w&3>3=siw!=4SCV_z5Z^K;k{Fc#Us>i~Mx4BfaP-UMefs~@KJqDZDMz$#nQlr=y*P)=NLuSy@;z^6XPo'
    '9}Gh!>6=esciszfY)d{xc~qz*`21_?!drvNTvk1O3>Ksk+l6Y`j|zRe30J&cwVD&x>~DO(w)pKNU&FG>mG=m<QLo#LMLqKsi}NEW2lqrX~4O4p'
    'm6YF!&6cuy(GS}fo2_81uRa=$Wn^UQX83m$~w~9fSt;f=j}Gd1)v$uw)=Cc*vWCOZ&;B6lc#&G(du?esB3lV?y^^Rs2}ZYdhH~DN1ByZ&@U-'
    '9can-)D@`9>T|Lr++R9=^pRiy00WS%Qcy#mEPVx_Bexs)pa@e3D8dnxs4Nh0Kjo{Ln;&GBejGpJN6|bGF;bfHm06y&Bw1wmqpQv$s0LdIz-'
    '6jyLw@4HlWTCbJ*d4D`N&%rsS$JYh<x>Rq&?4~&RV!r7uQuzjo#wA;53+o?5LCTJi+QatTBz0<1VggMX_fFjfr36zrIX{ZY=)_>;ck!=f^OJit'
    ';sC`Xl56X+YXK~*G?{XJDsL7CPK|DA|*@&oxXF}0)PYmz)6nqkESoc3&n9t_?cD?9XZm}6^xNAh(~(VzqDo^>Cq78L#9!Dmy#cq<&!7J0|dwf^'
    'Q*gCxa)+X0#DpDSUMZ3iD|gpu6p%4;IiAURXp_)elNQ|qm6u+)2oqX6^BJX(is71y$Hgq?9#SN%?-a6=cKoRS7LYslSS5-'
    'vE~e;D?}?$RUb+g{q?Xjxp<oUJgN!514;`F7mY2_#T~Y{R-'
    'ENp3^Bp8nXZr<z+3hsw;dsL5WHBjVmT#av?YbVrf+B=4J{vhK__yuR71rPVEG@wEuM;4kX^FqOW=ScaT}zHTYGm73KWn-'
    'p<^jyu%ers)a}p&$f}?f4J_2`Xl|BgJBn6ZsIDEGoWc(<Nf{pVdlHMD47U$DBPCmkpdN`ecdX$+gxDa^DZqxoj^Ydr9}zyJRhZWxB_ukEt{I>J'
    '2d8t{>b8i;`4Hbh5pqPgGq~lnu}L3s8C$dq(;Kj6Z9vLwlFoilEvT|_uoC+#yWE7$yl!qYbaDeg`V~b%Z1#%9mX_z_ioDQm!x6aMCYOfRoIrCJ'
    '&XZ7pk&gK^&fmx3-$1Ie^++VtY!JXvs0A_d5p8I!y#vkf<W7#a<|M@=0?3|6Fu!gK5eV?$9(3?N#ZKMYdzX}-'
    'dp9kTT%WM)Ou7;|QSuf?;H?wb1g(qG8C;$$tZ&T(ox1^p@FhPcbU?{j9;7XseNoW)XEDE&$+bcF^U`@|B9IVtsy25LUECV0;r58(@E1wd)psF='
    'D}NQyngCL#)&cBH!D8JR{s<r(q)fQ6+Adglsm6=ILi|e<+yDV=2H1WlS$35#JIz*vn!~$n-'
    'COCT=0ZGgy}4Yg^Ty0BcN)S4k=PcD{7V@1Bitmoo|ZtB_d?T<o0=zqPsS9qQIvfUEK(7qw#F?$b>^ffmbMoa`&|MdMWg?HcInZ85}G5A37vs-'
    '7K<kRY^8}9Doi<9Qu?9w>4{uA6D|M?3l;<29a9O|E@zBeSYojyLLW7n6+j}|!!k%tx-=26o}hW+GphM`b`(Jv#)!F-h#-NWLE=60d<1S5-'
    '#`J6dh<cN_xwxno|rw>G(de#S+UeQm3op*7Y#1WYF%Ad1zb3o8+-'
    'v_0m#GKK!I<Cn03q5j?u*81UoB6xfwIAVuWugn^uUa*g>40FqP<RAczS<bEObnfL_tK`kI7E`#QZw$5BKO2b}}(og>iC6f#5mHH+1tpOmCJ8lr'
    'kz-ZIcc!!7P)wE&N@FL(>jzyjc;AbRZ+VWu@Y(i0<?zh*KS>M__Is+^RcHBnj@HPH;k7!f-'
    'ix7(>^+i=SCkP5Xu;Zdc1gb8@{5ZT7}2aqnQoFH&Ij1c7z5>_2O%2RWH|MYzekndwyv=4Cm{dxGo@EZ`jz62!u9A5p$Lkph29^SR!<y|ZV|J{S'
    'n9}WLH{GV9kYpVV&h1PzcL0#!qG&Y+%xeVLNTQ>wd;GGy-kB{`v-'
    'c4YZP)4p5j01@c%6m_Rf$o9i*KY<pVegKE4EQ_NEg@=Bq_M%m2UPn$ank{@auSm?dpo??7UO<Gt&#MDCW;3jyu6QpggnH4rcxq;T92tDNH{pSy'
    '+0W81@028z+ymnojNsg1Z4&ZyOy9Xtocl64M$9|gR#`8*%@_sb5p~QDO!6#lO8br)7fu4Dy=k|9i(*s@xLR95wOkuZT!SC9t^h~_EgwWg$5+$k'
    'OCe+_dR(z41{tX1+HhLxqG_z{@#0R5|-l>J0^bX_>A6>d9bh;Pc{Jg?+*V0`2E-6zoMn|gW-pS@}CU9!5Q9#@1Fp=2S`3KN1^ZEA>3Ks{(<m-'
    'nG7&}K;a3NIEfTKApgc4#{!JKMHTN@fYr|keeNTEk))vWCIp5f@f<LnY`J%2`v#7Yz^d8XL|bt}EJ4^fMsZJ!p6H@aY>p^c79UMWvVzBIceYSM'
    'W1k`+pBD?$txZ$+!>y1e)i~%PUeMSP7~4`6B-'
    'ArO_gpcguVHnJ_=F6r=6e;XSc%crreg4V)GQ|Q@w1Sw1axXs&H{;JSH)w8AAAkZK)D>GLPBv!`mt8J^}1{hINEv*r8Gh|+}v~~F%Ba8o*r<qqq'
    '|0caCvUjMn^eaxi2AFlemeaS8}8NwP?kx69}_v?t=Fagz*%_<lqU=)^~)tS!IRTmJbQks|7*}3%0Q*Ft3xP^%BA)`)VYh5y3#P0QQvkk#GzEp`'
    '&NWgri7^enlh)DHjSg6$yl;K<^?{!6n1!Un$K!zxbcY?Gc#!E7De-'
    'aW<ND(R|?0S|Nwl^jIZFX1<)}bxO|N@c-n+ykEVDSE;NGNB33>B(2EA4&xXXJ0GE`nngci;X~!u%I(tPB1_&vWT2zHOl-oosUZF+4KT@Yc9sx@'
    'j&3s=9fok)OU@!%nH~|Zy&r=jwpdLuL{!+}K!OY^1Dbh6P6-'
    'rq)I}hv^SbYj6b+1du_G^KabXPxb2Rej*n8hmo=~yOeK*jGiK&K#C#FKr_HH8xY_-VTp*Ev!sTeY{wy+LuNwcn9JJRDLge?P7UU+5U+=a6X3rI'
    'XpExh!?#Z#Bh*v>V8$phxBtUd*z^CPog)<G!6Z&>kx`i}nd*I<O-'
    '>b#k2v)Kxh&^!zHbKra_#g~DpULuuHf?zpXZv+!L@Zs9qG|$#D2%pZre<K^L7|^I=HS9}ZhFb?ZS!2V>I3E&T_HG9nc+}~eQd-'
    'sXn_*?1-^|Km_5n^U(ZdR0)Srj{j_zh3!TT>seEXCHxO=A5_9elaoK{&5Mg-puPABMwIEYpBVWl@E-l}s73wf-'
    '(cm%le9*Q>tUqGIB<e?k!LP+Ac5*7(+59FyqG)o=RzG2lLW5a+(Ay9CD#|sT_ehia`ot(vVL?>w5f|7{bM||qS&GDg77ITkJ#nBzn^NFFi43H!'
    'VIfQCL2&z&@HO97gdmkah+85ucTVfI^JRR=R86uhMhH=dGLni~&j>?lk-0N(o*-9x5rzAT-ZO+1yUb%eg^smoeHr1R)<ep%7skxWWy?PcZoxf<'
    'FxTNOPnw+-'
    's`FzllHWnGNNFl^9mKs#9h5tmR8_WRDZ}No6h#HrC%Q!N^E>T2Hec+KrNcZ30`Y0IoC|O4z95Z30DB>r3=`Si1vxB2{YUQP{g&C(Ln0P9tO}Sn'
    '%Rzx!dlS?BqD!NuHhxO6X=1EFtSsm-akA7lV2K<p8{_PtYK_g%@TpQLK<fl$MODEHqFSM)}-'
    '=J3YbD(qoom4TXrTJQDb^bd1Bp{Vo;I1Nslc;N8fQUm-8ROcEKbxL9er#nWHJ4L>fU-#8Bu2bV!pycJM*)#RL&!tY4c-'
    'RAwL^TIlpz`o*!v^t9Y7v&hyudieJu3JL8Dxl{T!7k<`IiB0U?Yegp1l)h*%JufEzr7=J*W#Zs-'
    '7fXuFEB4r+_5t@9yqr7r>KU%<bgnCi2;^ywpdx;y+tTM@x1;#Os%yu5s(5VI;Q-m^&mC;;F{#n)5mfFmRspvqD{A>rjdG4=Z-?fp?-6jI{|d-'
    'S$&=S6)IqQy<s2OkEhI4n@Yq9~yKe_R+=a%+_DO91~jBq4mp8c*0JsO<Uk@c$0~qAdio>9}?9j=Pgn%W=Cy2<`;D2a4SW8pG{kNP2W)v~f;I2!'
    '>}8ol!;r2-9K35~qR#;l2dHPXOfztd&DSV4e-'
    'hd4f!ZSgR<MB}rcD@&Sy<ngls`ApOY=&MrXxnJ%ZWh!JQ@L8^8}pg*de2I1r6ATR^Oh##F=V{4QQ67`!<@FYcK0z8j!M9~#@8ICi2=#^&H>5PN'
    '%1?;*Mujf1@WVJ)6P{O>cz<HM-u`3-WpP7rmy6lIHXhKx@QG-'
    '`h=Yl8NT4yUIXQ)j}x<X%zt3VD!so1u%a3)y`P9GSUV4DW$Wno*cNRQ(jg$`!e?5P=_D>>g=fs@OBJhbEsp(qgV&>b3H3cu*EJP_vIH*VNc`j>'
    '9yNC>vW@Mavd`w99VJ%}`n7JOVUQR+(a8GYVxz=^XidFw4+0EX9ca}&WO<+ppfpF`LW9$jjJg3|L^a9q+J0U3Eu(@`Mv5J#2(PX=6GT1TExL>G'
    'FINJkLXCFJDv<0jET5M;0WE{b#X5D*^NgY*W!potFt`1o_qaPl8lZ0+PYe53DQ2wlmxQiGA`D?fh~b}y12w5+$mOD!COULNVuTFu*b(N+c62qt'
    'zNj_H9EtDyv91P*;%P6OR?)y`4drQ<W<X|}vZ7QdnU90nBh5dxLDDBRfmm$)e+9spFS-Ca(Z`$YKj#d!?bxL@osE-'
    'c+S0&6HtsX}85kAb6yaS*D2mM}#tDDyjLMGXnwoG7R332JkMuoJwH89iXjVoDEfXRC3jG%y-'
    'fpwHUEUK<T>ISf{J>Vfe4f?ZG^;rE}>;dqVF#5^`IuE1YxB$1K`BQ)xgS6GkCx>W~Qy{=f+RIcggS44v28#fjS5u6YTY0n$Ah7M#(+TtjLSP}z'
    '9mm(v9O`xfjeVN}gnWIN(9JCBKZpZ}z1e7mj2}Tnv62=^}6MB~kVgdtY;_y@8kZAM!bof`?q4(hQ^a)6XpAGM#rul31%VcFxz~^@{=3RPCng(0'
    'v(1vH$*ib;-'
    't`fHcU7BGuBn2Yt@drZdW}KFo7DoldpGui{dg0Zd#4+apJ~^m5G~AS$^@x8KBTrWNohwg3dW+j6$>W=lKFj4&mf>to!$O|*rel#TF0^!x_3F6`'
    'jztN_2MpK0zxi(|)2CaaGp1;gIv)0D*Lo%VO@)2j#ZiM&$`uPI*qCZM_iOTIu;|FAgbzP^!OPt9&Wc9Hgcp3wXn1GrGo0!CsNqEYa*YAe-'
    '2+ar3AN!!5Jkk>lqn)3xiTc;mK@+pv(d@6Yrpe~g+gm{Rv2?T%~r86fnz3~FT?zHiy-'
    '4+TS9*7=TLLJ9T*f%9X#hY*!zQU#a4a@NwKWoL9vI>%))P825}a;QUN~mb{gyaH`>QPS}$EW|8iCjePxa8V-_T(PM8$E-'
    '_b$*Hnxi=@C<p<(|PZj5iG(q?}g?j=3`=87X@i7%FG^#&NM$N0)}b&*>PN{|H69YF`+3IgTE#7?vo8DaF;gRw<9K~k)OFo%>`aUS3f@ws6XXz&'
    '4)+bpro|gq>{%Xf8Ou79e=b&3sh`)fPi?mTt!=GN=CA<A~T4W;jksvW3p3$*?_1I$kK}8T+mJ?6uXm>&IWAzr@X`<<EH|}GrSNqSTq;}vyAG6D'
    '#`$%;9!Ln`5Yy}N`zK**{3avv+D;L;8<v3r--PY^IBX6v8FE*=CDA5?{C~N65`CN52cofgsbU6NkKT0idoXWws1L?L>yg|{eK}8a{sQg{tr+RK'
    '%wBz!~X++zeV#BS(d(LnILe(j2icN_mURO2&W*2=I>}9iz5;sC#rR53mQ6^km-oHx-cIJN`bL-WVQWn@4wP<eGr_yq>)Ix<}+K!6muwv!1vHo0'
    '^uJpS<03y%z)pCSiS-47UCH=R?l)2PJ*(CO2jxF!JDiopCXk;zL3M!*+#%3JG_lb3jp2sbf|?Nq<o$yEeG--ojAq_;xQde<gBPgn?o3)T5epwf'
    'qq0p<x1G!D7)&{SVl?PBt|n$MoKJ9;JUP7J3UP*iRL%7`*=KqrZzCp(+1JRN)rwZ_(1=d{8E6kWWp_x+3W}AFBFH#UUo`1NXPykfK1CC_{c{0s'
    '3?+5$Ll8qhj$Pbd$*t)CR0U`9Szg7rA3CnjBE>&HPJmUG72QV8m0SFmH05n13=3BB*K=U6^e(J5qPrZ$|lzO48{k1*1^oKG-pfOFmIs><32In_'
    'c()6d{goON&8q9r=G?57dcm?efk1&+q17+hJSy3`Je11)dHQ4Y`$cOJOrdta@>$A1LaoBKv0b03p=f8a*miKPKLG6gCLL2o230^LO}F`U0PwNj'
    's+u?6b6PX@8^*Qn|Jv*g1Y~0>EVj#{z&y^iM@b6jDOe{yvDXd2?Nn|hr+IjYJEpQArn#X@)23frJS&fDPEr$I=7srlT6yzB=ZWxLv|T+@QbZJn'
    'X^X8BO`XR)v5ZPC-!uZqETLqgdiTJjCQP_CnB!QnZ{U8wiNQmK`rc$iM6!kYQ`=T%fj+0JAwjtdW+<s$MM5RfaX3(X!gkdc_TXyQ4unXJd-'
    '{crs7$+MLd=$BMngkDBRLbXz3OU@r0Kunbb3JZ5KMhNGB#GX#)oQjSOJATe)yxHqU^pGJPa`ng`0+oZ81%kBPbp)nYD5Paefgw$&JjIR(RtNUb'
    '4XDa{!&<Tidltc~XMjCyC0G3$Fl`f*R+AzGS*hH*(j6B^YlWTTtpoT4P>zeA+*={_}7`cX1};EF#SSzgalI{Y?lb{kn$Pil%gAha|j2kzgBo(^'
    '@$K?9G37DC-$<|r4Qkxl8@R3+1<TxyD_jjkRfU?pb97GZG;`vO+-p7eV}haW+cpRj~^i-'
    '(=meoQcQvqS2K7?LtYBt`IiG#^CJp4|%!`=8=}<We8yf4HY8+F)12e*PG1WqlA(?}tQk-jaEPq<xHui=bBGyvSbs$e-'
    'AOi_}Pp!3l4z9ZsAjPT<=(Y%{pzNzO`u`a=qky9s>|7dL#!q!Tt1OeL41mjx}#tVP2h{opQAWsVXS{uh*>3jq2yQOw&8^6>9*hYD$$oC9bU?Bh'
    '0&K?o1|%>0-jN>+b_v^@Uo(0S*kX$YZcg9Fe-rh?M|jjshP$k&=RhHtSKvpBSqwua}X`Ooezh#SdK1A+Vp7I1kH2ZZG)rvd5NCAkMNa(f?gBGd'
    'M=w=yl?BRT9qq9Xhf;V?0b*g<|<6t2g&3HcwBhatk^Ju5Ff`K0r~fV4?Z0(Zh)iW7vrzr#C7Kaj>V`MA)CU^nV<5p-'
    'G;*}+qDLa0^Fk}~b!BYj17RJ;Uc&;U`%RoY$gEX6dfX+0^2dS|L^za_+Gr8xR6e=pJuJ&5Sq9T}~IP!Mt$s&R#(s+AKx+_)jkEMi=V7H_<pCcE'
    'r5L^LR$jq#<;r{4p`PUvDs5Igai5KvGbMG-<wnw|z4S0(5hDm*ErL~q*UOnm#=C!R`YXF=7tR+##dR^dV93QnZ3-vmMaB(Df>AQD|<o=-'
    'dvB+<$5+0#DiT?DI@8|h_eWa}U^To&IXC>*!|>6;1f_}TZ`-'
    '8$+hVx1Qc=6r#E7awb6Dad<(b78_1;1c!?XjWTU$s+2c;se;DDm3;}_zjLaP2K@2030)(Y6&@nqrhxP&E~vOGSUHy@RC4B=&X2NDLwW^P9zi0z'
    ')zJ+eD*mD(;XRSDmydJd6HhPwL7^^b9EJUY*iS)?L05y9bz)oXDD%!E(0H~A(`$Sv(p}drgEls)u!8L&bsAl+N+o5yn0O2O3CWLXY=l5n-'
    's3lh)|JIHwa22H@!#)|3+>^LU;i(9nWmEh643Kn?T7>F>@(&4bZ&U(0%Yvq_g~#oC^Ql8vfhx6At1PPVirgj~vp7#lK`fx4TqO3)WSc8`yCDM#'
    'N;TJex_qONm`$7`jO9p=;sB#KDeOsV?SQM|yAMjAZZg_LvZGY<3_pbjcBTpxrwa^Pb&h8BBM>7K9ibT>=EO*d`qST9~+jc$^CU+Q{LExZa7MCw'
    '3}#SGdEG&A#{=`z#q(Wx($2C-'
    '<YaZltGcoWv!0hwd{+EixHx3`&2|r}KF(aYWkX0|y?Hy4zv&kb=PHfcVnj5K#SO1W>ml9Bw({kLoNI=aPcD&CZ!{#DZaT*CVA?efK5K+7N_e5I'
    '?+UM}uAnym3Nq;s}iP4*>*=h?VO3-'
    '{iSKMD1&e)e+NAqI(HKA9pSyD@FoB(^!+jLlVWo!Ini`uW?9R{78#Nf1giwd<I6e6k+^{orW&nh<4pdRsgaZjSgvV({aRz*ELX+gz;@no*kfv3'
    'rf7OUA`ql_(RP$e*mSIkTo?Wlfc7}&^e%#O6Z_DpmY4TX0ub0^$r<k1_@zMdJwi5QtV>R91k%vu#~B*V-'
    'FfOmu#7f>r*=DWC;=CPH!`~II+Qj_ehWPwj7Lh5HWpyWWGR>Uo=@YS$tvJa29Vk({r|HO5z9x@(~Q_b1c3a<W8!L6B-'
    'E|4HKKWCp<U?>_ii4Mz9^>!8T@*yDuP=NKWyca0<C&kLUuUY!ccHixBq2&uzYmZ$x`9zIM>&!a~8AeSqd=2+F>F1X6){_YU*|9LOGv-'
    '1SA5NsZYo3?vOiqL|8;#Niz00L$>&56p1X;~c-_(Xv(pS)2`;iQ!LQ!;5<$2Hymv`>U-'
    'I4i!T_E(ecWvZ%~MKAnCij1W7*N#%Qv)>a4c;HA>k(M2b<2FzO|S^Azj{vjcxN~kLy6YW+-'
    'm_$9K&H8qX3L!#hNfHqzJ92zESV$GqQxOg@P%+Sk`x&c#wJT_Fer3EMh%+oY%U;7<!8<k=7v(E^L}DM)9>h1=sN3NH9NMiz4qa-'
    '2q+K}gd_rMMI2IV=+d|R$FgZ?XC$w6D4;b5qU@qupL=gutj8B9+1sgzx4VP0~--'
    '<wwlL*+l>$t;(zGuY^Y4)Eb#bXAFVii&}u!L|aqcwDG9*>lLGGyMx07DFwsm+-N^yuR-)^4-p6p|wcnk6?djtR*V2C(E{-'
    'dkE|ecDDYNz`HzXXjKlLWLgLX^5jYh2sCV+4J6Q&NuLxVHD;hmoh<7c*XV3l;wI5p5lAl@K>fY+_%a@f;>SePwUgbaZXEy#u{>!wMfoQTSnPI!'
    'lFyVvAGFH`XEXK*a7hOgBt-Qp;R7uidY^lKG7hVBc1jP@4PstD9&jaC0$R1X_09XlM_7#@s>d{14LpjOal>W%{NJ6e8On9PY{?2P*h2+0LX8Ng'
    ';2Pn#kn{_zah2E7TZxs8$yfxw!U?DrJE#KiiMRpCRSh4N|8vzAeQnSQ_H7&?_z?F5sc>%Ir9vJ%5ht!hUG<3ykk2iO$Y4;iMl`$9_mXA>k&^tr'
    'Ji;Kqy<$XeI7aD@Pa;K(?B>2Yv2_SkTB&_tXw*cu*txAM8>GHnmGpg--'
    '~leH~>hFQlyVnNpm<OE1e=9q3gGF+%bX=W6<1*Wd+i4%t+A_L&S9&`l+&;Y%>-'
    'pKZJyiqk1_pnEgCa1YI&tKG^54|M|4T&W3!I)SYCk=O(^}SMTWL>~7*wYbQa&ul)IVr_q(Lm<C8E2@xO6XY5R%F;}M7$UHRag1m#sq{x6NsHF5'
    'GRz&hH0Q)N<livh6MLrjKMKBlKzlP(7P1!OM4lMT>+e)+$;RHO@6{d(hU(<q;EEf<%jdHz7>GKeJ52an&2=R78=URkINP-Ehkc78U>5S|>p`c}'
    '=i!6Bt$MZ*mW$&uI*1;W7aeG5iK~DK&5W%wRvkym%E2ba_!qEs&;Wqg@gz2N?)FBxo1Z3q=i>;ESTT7+QP5}bmOfJM&nVUaWy^zrQZY0K7%3Lh'
    '%KUBA1SlY1zX6Kml!o#FUae?p#R_K!IHwW-'
    '*7vu~Vh@JI>CqIKqIN8L7pwp0)OA56voKiyc>#JnpR*<g{SrZ{PQc!hbR*i|lJq{{mx_Ah^>j>6t%2E!Au!=p|`{t~YoLEq`z&xvqcS8Exkr^@'
    'ZOqYn=gV+O^!dWI|&*}Mf#d(=x{?Lm+dev*^=tX?LL}oyY&%&o%r};{&B_r=*{Ns&8uXMa`QQoXT+z#Hr%4{qDgI%&&>+UHkXlB5fKYxn6s_}m'
    '8W-6-'
    '|Ik00G1kAc06N(m>yod`Yd9%x06PQ;BiXtTY`=lmr<(R>k8H!suEg`YYQQXQAjqfKYA4ktFq+m3nwg1rsOwru+p9=CzUEP<sj~2GXJRNkW0p0k'
    'amI5YRW_4Y>#$ECRhNFBE(KfZR({L*Bxq?JdGs_Q!1vL6H3&N3JMN0-9lb+`v%fCQ@3egJ@aU!^D`dV&_ZQ{Fkq5&Z)&*84*Ng+?H-'
    'SCNCX5b@Ic~eA{T9_D*O|&S|jY{Q!bX+KJ2}zNx3wR^2=|bge;R-2fD$WDA#|nM4NBu9LZ+}u&-'
    'DLs!<pTkJv<F6<8DgfjIa{f<TXlD<xKj5vXJ7BO@v0}8U#<vSuk2-)z0P&dYs|X!+G>N6Pqd3=`0V+!t1f#x&0=**K~NNV2-'
    'J#xA)Mm2%}i|p2Q?Dx0+pJVYmBzwF%{V}rgFj=Dcy8lM2jZ<>BUE8esrLWatS@3@2Cv2A>wiB<(Ee!aZ?hG^4mU0))>QAMJAUI<wZBcu$kA~<3'
    'MbZuqh(z>*0ULV62$iPVP&oOk8*)(iZJ#>0Tb1HMCVT-'
    'HyU14?dhFs9p}3tx*GX;ynmvJTz~9ZOo%mDIVMxDU|0$zktp3M-n+7LN^l5{{+c7R9tnCLgO<bntd-'
    'vre)Va*%a3EkI^(8A8RQzVl#2XXVoz0g_O(}*)?RAr>@^_`o#)I9dd4s%V&R+J<{_r*+wX*g-_Rh1?edQVgy8kqNb-fm$WRdZl%*2qO1?Tp7kL'
    'n9ffbEqc~_Xh~lWMFycBOl@=zP!zO|tiD_Z9lEN!lI2V)5p@NW<>#|Jya@c6@NwP1S+keFVd>|7~vt?Ni%NUS@<gTtn2}L3aqcrkVJw>~0Uk`_'
    '3GOS<Kv!i%#*c3$Sh-XUm@*`h&vUi)qxpiVG@7qWumLI?__?+~%cPXve*HO*wL2ht@y3gpeOF>nJ9zo~>eiTXiRrYR?tahK|z<N}<)B*sJ%vk;'
    'SX#anlyo7@4%&a~;K}Z`LvN(CWEb=$01QC~$K8>WPmnFZJdEZBq8M%H$W?K7_ndIy}E&Z+}gZ{MCElZ)-'
    'l*BwKZ4RX+MR_iq&j;^FE2=Bd`YiN?3juOHK<R=&ELWY_immJBZ8N*h!RS@Itf#wICy0CTZr8()WV(eX3RNvSs>F_83fL;7W0&NtZ7MSeZe6$^'
    '&G#0OG1#p|9czgy(nw@Fd#H{Fr2+Z5MDkIYyG>n+L9&5}h71s0sJ4vk!$HiO%;v@kjfvBSZr^xBd-ECVb%LyAEN2E8l4(B+a!CMD{#?26T}N6@'
    '3ceR8k%pP~Y>ZoEgkoa$<?vr+{+<1<kV6%7aDkqbz<0xN8aO6gpT^!OXtpm4@swG*MvM6!CS;?tA^xXa#zT{hBgliW^Z0)5Hg|#Vyl;h#JAw$l'
    'AL~A2CP*LYL=z#qBb(DNeoJWaEYiRFKJ6$PmpCp(sKZWfi5blfNZb%nLwYECw3m^VXgoBWm<x6A5)5mju&)bZn-'
    '1Ga2fTQtP2$CQR&dvzi0KL?!Wp5=IXH5E6YQ(Nd4T9EM%Ni<5aCh}2XepW$$S7Zw~Dh7QT0STAn_tF1m}yd;XTN4UeV&@E!`eBa!p|5QNJ^TaU'
    'DcXr8p@(=1=_G3a*w2=d&Tp>D!#PcUEZu20_k`T{GcwAlr)QXtsWn_Y13>cZH_?mb~)-'
    's{E1S=XI?ssZ1@IMoOck7K!V+lsihmlQ#*4D5EgGy{!tE=jlK(flC*|&5u!x+2PWP#p*0{r^>@5xQ$a=1lRlZ+ShA%>9~rr$@I!@+Y2t;Eea+V'
    'T;noJ1^Aj>`Blrz$Dg%89a%<Cj>CmWKoiATNaH7Q3$3iE8v%lGaue#-SXtQA$;f`h6|kyB<1E63)V-'
    '~;kjd<4g>V~%M_<oS=)2cBZ0UJLl`}o`FLhfj!>?4kP)`^rX8W<_#2wGGdMH#W6bfYoP3cR$+UzvbysS`PR#osgder0{&nw;`)3Az5<;gb92VP'
    '8Ypi3P)cs5QHLicXlBGnOfj{oo@Ldx??jc&a@i#f$`xVb9G93}f_<MtR8WN6M_uQe*o>$!FrhFHJSOy?cERo-oHHOiKT)GNN%u10__U>oFxEV<'
    'X+TE_x}OWWh{?>J+!7^Os?NGXMA!Aiui+>CKliZr4CZ!A*PZB**sX;{zG@Dnh?tFxVJ&D$z@^&AojKt>90!_J?_<W^er+lE`mVic?;Qb{$s>%a'
    'E4+NH%H(+nk!F*17S8973EHezxp#HBzGISf={0zKn^o<cxR1fWOq8)5n3z-2Aocqz!1MTxIUVt%1~U+3LU6*%f9V8{guHpUC-Gk7CY5q==(5Td'
    'YHBL5FV*)K`oUMRGLrC`gd{tRc}60A4;nbp2Z7{Vv~LqUHlR}FAxcxhy1Q9=Pf_)HD-`^IjLAUb;Ep8-'
    '%sGmH^#Xvxsbgvx3shf{W88U@(0?^`k(Cn@Gb=Lkl7Xr1yr<v@m6PXlD1Pmi@kX4<*Dd|ugv-;r)VH4`(jU#w;)H=HBQi(UdxUl>Nm-'
    '{OnJ5;n4f7jRUYm7;y=;=&c%!E<@>R|^*}<l1!SJC3F&5~~(l4vf!h7mXlkhjo)h?Z$VEEYHkxhl<k7in(1gk~Cu;V<^&R5$2(|&~5vgp7G7h1'
    'V=>LmSl)K!Nkb4%9s=xs09#6jP%U(M4w)udyQa-stYxH`+y5bEw-'
    '<d<jO3^fs$=0HvWMNW|v)+l~0P}<$AO2iSMbo#HuNa$Y!cibAb<vo2CJ?Fb_0liVxjAZGu<J<{avRhsF1$jIvrs@}@^K6|3u&5;IQoJxTJjItA'
    '*9*uxp3t%GESPOx!_$q|4<;9-|YaW(hI1(9Oo=IBc&#9FC4Z3HkmVD{5}Q^g6hXebElkeRGw&Ys-'
    'AiiXp|;545tk#Hbs4Do5K_c@pf*c(YabPG+)wGNT|6Gom1+<G!;E(e$aZ8UtXrMXXKmk?QQLn&=#(p%M7C|_<RCSUFWET~50mrU-P7$A2quvo-'
    'oa2|zcad7=iDE)TmJQ$aBKLX+ZWLQ>!fcu4Ky?XA#J}qq28W>CUA#98X?7DqB2=~)d5N1ZlR#{_KOhlB4y&|+)-'
    '9ecg0)2o$D6{ENvCCRx;y#(tZS50v{1e1=%AWR(?mW!C{tId_vXmg{W<n5*NWyvM;^_ra;H*V5;Zl60yxlA|wJq&4kc(xS?X?W$vaRHltURAvT'
    'w4m|uvKMa6Ve{o(}@B)o8{O|eOxy`Q0G#=V8!k9w+(O|cC)izI_I8y1{?pwAU5{*WKMi6w)>GDthU?fxaBGV=f;i2CDxv;g!E?UFq%az+g9j;6'
    '{#h0ttzm7gu9l@`ey)Nl8Ue>N<}Ml8HJhf8p?D4Q0QB7b-'
    'C^~)>3LoR`9w3PpXz(rLv<VN!hE_F^_ufciwm*KQV=%{A~E4aT81U4wlhsIe9;Ife3Ke()}zRs%UA6^Hml%xrAX@@llYHAndj%zE+`vxpIsQm('
    'INCSiidTOUJr&;g`~647=ntD^0H9GuH6);fEQqBO)@4^duITB@jT~2#sUX7#=^m<+9g;<;b-'
    'vD^Bk9)++wv!N08r`~xVynL6C=|5P#>wu3!0@5dFHGe>87qT$i8B9JxdF`9tsP#cz;jM=d#61cF;cf^x9?A8pq*TmeJ6yn02+PcRik2Y%+xN+0'
    'p;*H8zCSd}Z4bP|RGH~lwLt9t2AZ|`#;8k-7FZAo+9R=dZI#dN>fO*NPx#cbW<`#Swm$t-ju6|suC03E*!JG~uS-;sdlh}yU&_3s|AP+c7-'
    'De1@X;%Lwv}@Z@ZJ5>$)mmWhDskSgcGm0Wp^Tfx!x-'
    '(@IQgH7gf5q)SBE=?#d~wbv@0|GBp<@U*Bu8Zt|XQe;{qJ`lZi`fweTXtkw!}#9CdR`PT#vLvJEPO_M;%eQaQ%l*KF~T%)N0pv>Qt@>O_W_1Bs'
    '#t|GKz5;&Hj{By)(Qx0CH4L8Z*L!hpB$5yPw~?#$5g;~AOGk}}7tD>P(%6nDwJN^>fT6q42>@;LbYsGP>3ih6E&Ge&VcQkJya!jU=R<fC2w5k5'
    'p6bR~`_t%M*RsaWU01LYMAw`8r?8m#y$rKVD34ypNGC2}DQ2UfllsN%E`bzK?fs8l17O9#dM%6vK8-'
    'W|$07)>uYGS3LJ_I7u9UGrxbQfIut8S6)SavZnD!O1xiQRCi*_Qn+$Hr_LWG&Yn%jxLs3TvS)IpE>tSLdkI>8AJG%rGzWwF%Q1bqEdm+&5ZLZy'
    '+jbbs609Ft5WW2Nj#{mmVREO$Z*0j>rzuYW>a{J)Vgr!xzMjVsJ>NIqY1}Y-'
    'bboOnL>@^VpxsRSg7n@_~yme@P#^~8kedV$+Gn8PxPEsOHMAA3t7)qMmocO&VO<6TFRuv3`N+BN=6i{MI^l&mNRS<R5m#sl$8dkiFhv#+RRW_d'
    'NQabV~~a>3(M;IDJ-hc=_~Sz#Oxq{(Y+#tKOmi<-weC~WtIf#UcU{z?oV++WRARHK}4I%^c#GS@e^GGPf3f-+(QW&A1Df0-'
    '85tWOLxUvS+U3Ht|D?(ZeB0V!9Vn{QJS+;_Sgcc=+hf0DH6pxRj;SvgJY*sc4iEINl9+j&d8tt;{Qtns70`ym+Q^tGa@5UnxeSy4exEYBoEj^-'
    'Fvp~;ZxdnQTd*uv*9b3Ulv~(@8CI2O+W#eYN&(_&#K1I%#d?iEw52IU9HtCX%`EZLGE2k<1Zh?ybZL@w!O|3kaN+fn+BZ4u0Seou4!HIC^F7;K'
    'A+d;CA*f{F^zfJQVSw9IqePGX?WMI7obpjQBpW%g8-@_^710V9*6I<m}&z9C%T=L?98m)&nOE=C^Q-ILne74^Y493tYj<!U$}-'
    '=h_*1vs&jOvCk(o1rx3OXF3y9t`D|@VyLg|Bbb<!!wt!HmrOI_2P*dAXh$M1{OU+~`mkB;5Y)K+P+SP*M9?O025@cHL#9ZXZm^)@?l#14gQIJQ'
    'q)k~SB+4yDWk%g8$X4k=<OWH#Fpafz>#Mo48)bMD6W+r76kC>X)Jv(YW<7Mr3ypm!6mpea=egHuC!tMhXVB579sp8T+{V4|CDiJS<gSa{b6|{z'
    'g?}0e*UCn5-qf?sv-hXa<+&TkN;VPPrtXIylIUlIlbBZ>&mCD%-'
    '_<_k;Js1sLoPv5ahNV}U>pf=)!@avv@^Y+Y%F#)o4WwyN`Ux$u9Tt9NdSo_)U&=oK-^x8B+Y_-'
    '+Nlo%+(JDV^wr|5u$zN4xqG5pIsh3~2=NDmv(4}}w#l_f?OVZA%`>ljWixeSotm>{<F<gAk^g`y+G5n>vmaiin!C5S^A3mpvPB1U8?rT8;E4))'
    '(aOv6SEGSGL0U~&_6#4hq^4>bqc$H8hrT1BngH^Bx`jnx6g(HC8JQWN^uXO^L)wNl<fWfEBt{<OY7-'
    '678T5Cc&OVaKQ?^*FNWKQqvTf*vxHihP8v$!;CXhFhGK5B=>4NM$rU}UBSB(|`2p0<hAL>D$Ez8*a)zrps`R(7<8Cb?5q+a&gC*u0Z_H{lf5TX'
    '0#KowPkO5}vUv8xtMSnTax)B%p)J^JvR$75JLORxpz^LamU15?hH`Jrp)X1f%Gptr;Fs<t*(L@;9kM?WMr|hvL>UKt(O({l!o>vV<evmU{i!@S'
    'H_Q87d&}<wcy(OsmpOXO{agVTMB!wUzls=Fnd8o9k!Au?6#ZFG|Y~P#EIKn7(^abMt~vn6F#deU>OQcce>(fasGRf&q(f!Fc1gxAgwdV3n&?wB'
    '3H{%ITNly=SP?IDZ&{fgzG?_Mjo?T~nnT3QpzA+d-%lDp%hRl&-'
    '!OdMFn7IjjF13~3b8<&@_RvRi$>>h5*0F}sb5w^D0(l}s<{m?!E4E}MEowF+$t?H*paTlp$#aglDoczA&bHJk0=HS3swR4%}a4t-'
    'yNS+z^3lBGusr=s;nsfEJ8;RTYIS^T0=FWoN}D+YYX9Of+ZAL=G8p8zNeawwN+{xD1j{zI{6G^oo2FH^vYgSosvm)#vpN#AD;`pO&Q=+Wl`H@u'
    'h&Kr@+`&#f*X>Kb$QaDy@BOEFD|YsEK9bDMxI(3a_ZtJAS~%wTeI<3<ABP&X#xERJeu-WETKwyeAqMzJ_lNx+hQ#!q%Pn<y>eB|HV4k?nLox0o'
    'j{%IER%#*H{?%mfX;lTmbT<`-'
    'xdrGL~Wr^6g)^dxn=mU2bUiii4Lwkzsf&5~|!s242ZdFVy>aR#sorikyvQC*sb@n1=}_M?$wHXDiKJq@w({=sQrC^urP?e?dnfvjrPH)eF5Swz'
    'K&AeTn@9oq;54HjuhGL4F~jB&z2)M<e<dcEmav~u#5Vo;-xjx0wX$f=V?pt_9p*yJOKI^~5Hf<z>Fn@-'
    '@B!cme|D6;9Gs}j4Fbc;?rkmGo^@<BfkIOr%(#{<oJBcbkyQ5prrJ6R?cf}=%chOg!;Z@T}An0h0|{SXLFTt_I6qNt7M3dwg+vlbr+KzX9P&CY'
    '&G2N5p8+6Jt!bo40x0h+JH$^@zd{1zw$V4SQNnS~9B|NcMk-iDk'
  ),
  'index.html': (
    'c-n1K!EVz)5WV*+mgSI39aAKvBH5NAxU>Qhp<XyH>q)$@@mjl+RJlc=Z~+NbLgEiNn^HtXY5NQ7U+9-'
    'GYnPHny?8w{Z{EzjolWlLM&i5zR^UWuTS+*W7UekQcFMD)0Fje>0w|a)gmr)^pW-OmrC{qV#RO75Q*c-'
    'ri=0VQB9w$WR5=!D4l^YoYK?7GDpW#8P6`d_4*$p8aY&<$rC0$ISmV)ZT;T0$7$8xLUjyEM@ObCZ!`%(m9GtYOLS@P|?EbV;2$nrnV}(MqtHl@'
    'AeDJI0s9E?6f8y)rGxL}JjDD8Qk-s4KA78WK;MF#JG8pb144yH+VtdbrFJ2xnf9lUdLhVnQCFP&`6{Y^{xB`x-YO-'
    'qblApkz{CV@Sc~3Foy$t+R=eSD<6QDv3*<Ee=-$e7B^3JKilC9OMlekOUO0+89G7CE84(A$N0YG<CSQw?eA3GGNWGt$xFP-'
    'Delwhr~L0IMbEvk1N?1g6Hb`6r(CZCg)s~J;y$_YW&5-h2Ob5yFLv$)F_X)`uF+fQ62%B-Kn?U}>`Y|)wjN<;l15#IS<VL-'
    'Mq`PJgvHG1v)zm<u}X|1d=VNq^a+YlPzunRG3Xzh5Ieo9jdt3;&Lj9it`RE^*8b}Pf2l^b%sp}ZVM)Yxs!0<zZudV!`R2-3Bpk%H~}`U?}qXM+'
  ),
  'landing.html': (
    'c-'
    'q~4`<ENlnc(mI6%{$8TToJ0mELN1Glsz6SsorR?Bp<<Nl7YoD^^QFQnzhHpJVI<k|6_uz{ZmV10iQ~_Uz7VW8Ap$qkT^P0`<R;zhuAfyN|l})-'
    '6fhCbP4f8QfCo)_s2O*FF8cAHMk1`5&Eo+Swd$b=My`jeneO*xOjk47W4*APQUXXDb?qPIEIHj-v5e=9Tl$<f<9*xEF3kYnh!+baBuhjx$cP-'
    'y26gXm+vF8gH((qMc4N%F!3s>GV3|PT0+jnqfCu^Yfn3&3H4~igL|<w?9;RI^{j-'
    '2Z7nP6^)w1&S2c>_msAOw>{{LqoMPcD<3;Y?@SMletL9edN{o~-8=fgIr{1JV0wSLH@$!KwtR?>sMX%l+ecTAt{h#P-'
    'hsc@@QE|MHNA^%_NF(FuEHz#;J>fnjk`y`gty*1`Wd!>uhV@t4D{wqA3#^|GCYOnYSROF|H1SS#<+U)A$y_joICR)*Lmv9xwGfbJm)%RpFj8FO'
    'Xu^>^ahM~OT0ckbZ8Xl{3i6Vk29U_=W$2IopCo>|GQV<{ik1I%Rc@p#qyL1PWMi)u)ZHTJsMxezx83iKc3`ro!*7|Dc|!OL2EUaYlTDj>V<wG2'
    ';gfk+_?<D7K5Nrfv;QJ<ET|XRW4P6Dt;gJ+vEDFcClS<*Wl|Q97IF-PXB}N-'
    'A*s6pNc9`qwT@hMt2*&7MkTCYVfaoyr5XDwQBUn7Bp#A+hL^&U&A-H!}_VP)n;$>hXBnH4iJ?aINQ-?*y>-bdrnXqTyo0z&v2s=E(Zm-'
    'P;tv;H}BQ5&~6yE>OnBLgi8o7)%~F84KD3I^4O%&zmyww-t6=?>W%)e6%BLnWEU}K0`S=Hc5{trGu-'
    'L)hxO4G?APWhe>@0VEqE(8?hooU=y|u%Z(W{jg~N?bukNi9(ARgu;WBM-cC`^UFKi6^+r1X;&uSY$Jl77lI^E0lvjFWw_xZ3l><=P07Y+v9C^x'
    '!18b@31ldy*uo)4QZ)7NL<EjROWw9${8SI%bKGef{XcNF$UxluIi@NQv2QQe2lSj7X#ZAP7q&2in&mrAR-'
    'i&5i32S%oLv?5%4*h56_grlfM3(0Rqz3m*#rZ?&DM8kF$HhHttYDK->#`bvJ@421cV0-'
    'M2qHfe2Pq4Ror?&}H81n{`=Js#|TQKN%aCQ7?z110ojc(KuKll3MT-b%~Vc>8wjxLRJt*8m-'
    'jD!Gw?L~YmMen1XjR|xz=!Tc;jc&hrVRzGaHv@OG;BFS(fjj~Ec+!o=FoE1?5H@kCxx7~_MO((!_|Se5Z(g$-'
    'ZVi@;#la=FlrNTcF1l4X<1E|Wi|nPU2ZIEOmkI@VsgSS0JEfBOPNfF#6qI)mZg&S0w#HMXTDekb?v7wjVfg|A*^&s-'
    'd=KF^e{mQNCPakmTb<rAkl*Gq{Pd`kbILI1tjhooKs}pX<vS8?kNdm%=yKE;_AkmU?DS|K+TG~VDgeMnF9-'
    'B?YgBJWcxtN~AwW04kpfnJ0;~$=wyYXkp7)Ee;dHoTz~E84KisNs4}exQ0pc`VL7I@2)6BJiLa}vLU|2pPe&omsc-'
    '`3^)l1%^8iG}7QP^ni<}Y-'
    'b7oy=rI{{B1=c#I?RtU@L+K@t+bN8w<=DwTfXO%<V3he>@F6H=)%XC&o0|!7xJ<yV^%|L+=zmnMS%BtE!8GctrWe~!VaKU5#$@Xa6X<yE9zN?'
    '--oi_lP7`+rEcAvJ5)5E$C;O_*!4l@PuRUASo0V9Bx9-'
    '<}dx(*#Uqkgy3a%k5F;Si>@dT|q`O|L{i8xRXt>E{kni@aYQIT1qC_6U0>+C(%&>_>eQso5kxNcz+b$I*|LbBN%wVY}bl9_4mAqYh9jHxF#k3C'
    ')Mi&3=CrnNJ79ervl4(9+-7=q7$`hi~NG&>v3v+hbys1-'
    'WM8VP(&)Ro$Raa`VOPDsPnQx7#4LVOufRJhIS<0{#q>@M)HVI_;a*p6`T;G(n+ID2B2Xy`wgu2O6@nA&7+vK3v1ouSz!TyD<Gy)y?|_xwm=5@#'
    'K67^R4qGvB5ImTCvtF%T^nk{n2>BA(LZxs}cE8DDXY-3&mpF<ixUr(H1bGi2~|{ngZ9jFk-1X>>I=}h>yiVPQ`H2SBMvW-pz0IdwquEu=oye-'
    '&}8d3;0{JJ`Nk(-EfHCM_fpV!twSHz#b3=W-'
    '_WTjp4^7$KQQq<uT`3AQ>PaKeqBneuT)eN#7@eR90~beU2c2<jo70SCMLXt8ao_(uywC3!b_o?AS^rSNxZ+m6`C;0^uar?sNfZf$?q+m;EYoHz'
    '_s2nzt0RJr%XuUc0!PXA^?KdhxW7SFH-#v?x&`v<Go)d@+i8M4O0t=DYok{$yTfM9Pp(VFLiyAxga-dl^Kntwz5qCRe~_?BI}>$J;lIfKqgJqV'
    '$<l=TWak!xhEkc>fM8pr^|&e3)titdJDoe?I$fHGwT8Q^s^`bRoL9obwB<Xd{~(wB8$U=9-'
    '(GZfn`k$}=e2=BG3bWYc(`Q<@gC+UD7DoA+=L7CM?}3{CyT8I6bio+0BYC>D4&9-'
    'R>AbdjXw=|d2v>mw)}wWQ%R9u6lUm8e>))#h=sykCyCc9CT)1eHiFO&KIbU@5jrjf%I+xe-xB;3y!&0|DUQCl+A}n&(0iFh&dG$u83X8sivZNf'
    '=j-'
    'mVIaJ+LLs$s=lkxz@QM*K>W;!*RW5d3uOELM0Np~;{Yr1bWlRn2)nrr{0oy^j=J5>U=%sw*r^7OI)3$0_f)$8nrPec9(5J5!6}p<&AJF4Kv(7K'
    'Nc&y<2Y9QY;?Q)UWv3+<k6%{tpB(Jg03`<GG22@`5Pv|SXb&AAlx?<uB|OpO-m-'
    '2T&@;G1jtVKPlXgS==0sau_CqBd_IL=eYLk$ueI7KaNR<_<R#{QVh9%lk4oqdQ+^!b*TCLzg)C`5JI!RiRges^~@WtG7Aouj!i@{fIkmy|Lvsh'
    '3jS*et&VS>ZP1L{O|)~HqU#h5*p74}??2M?kes0i9iAgKdPh2#EEysL9|O}J>)A}^|~>e?#n4Me}~uscbz7FE)w&7QNgU6AHRo50Wj8^n}6LmN'
    'VKLqe=R6_ui}9T<Fvuv8Q1&`{!3W5Y_-EtcF$nIt+BaTJC$?2iFQfF&VEO0rNsZ7!^+ll3ApL@9EhBrSw5$cr9Mbl_u?HEc42@Y)nvuY#nV-bd'
    'S|`nrNzjiBkZ3K~ok1BHd>1|5a<%!1dl&K8vJqoCc4n%WTu<zi51T28r8EH#RedCHz5*y7Rpo}3?Q+#CSQQVuH5)wrwe2zV3U8ouq4pfmYl1Q3'
    'C=X)<4YnlJj%e((+EvS;9{qi`l~oUdTye$}s4)y7Qdh+7vdrT|b;ODJfh3Jyfb0fRdz77gU`VfRok()KHAw<~R5%%@PP7D^3ciz`XHi)nt!1Hv'
    '^gOcKY=I0ddOYwGF+RadX!gsBfgMg3$JID{Z^2+W=lcbVK-'
    'M#0q<NWl$AH$^PL4uY!RD2TU5<7hBih(iN==Ks;WEAb4d4>kn_>Ww|~%)={1jdq}Sk?;2=X>u=X*9{v{cXZr6uILQ676WlLtX0CQ0wQ#pgn-'
    '=+sKUxyWRKA|3XiWKUr<egC)3A-'
    'JzT&+A>PKMZU~xT&@M?tjwey?hNCf4Dki3ADf;o^=DBXv9xo<y_;Q#IEP%7hLMdk7h0+2CUyG2LCd4s)Z{ZVcj5Y;B>y+~#DMS@LVu?g)g*0WX'
    'amiM*U5VOKP$^f#a!Y+-'
    '5QWXni6I1dt(xRejVka9Wh2oEH;WloO6s<cwi_v|uht05jgn@cRL?iJ6Qc2F4%a1XD;;Egh!1!3AY_C97vZoK%S>SdplKWA0|bJ44vqDz97GDH'
    'D3&4u6{A|)GY`FJia>Z8PB9jNif++!%V^XpXJcAQe6(r`Cz4EB;4&dC1x$VCi`|TXv<u*@#5M`L`FkD&CTJ6S+OkP=o;JJ&p0yY}iPFSpl1Aj!'
    '7A80L47Iu`ns1>sGkM4a2=!cmNJ1p7Ag5FD6yJa+cSk*G5XFmas~D6#1dl{kVIIpdGaK%W16auQRdkEy8ey-sfZa8gUn{8Z?Xs7dJ?y)(fyG@q'
    '(wWrqTVbT>PDP_>^4Ll?w5K<?6>>3R>&b!mYbqeowsWIE3<U~M(uQ+0`iQn$e32rRkMtaLXWuK?>`myF21pjKEv(89BOsjP<$?>6LY6JX;J@TI'
    'mNtGONSehs$wUIxJA(SM6Vyy9LF}Q`88SCeolVDLc(m$Utc`?YCm)nXZcM=FyFTTaZjchQ>Pq^@ca*+l^?ve$@Up>{q6%8nwMNZw&>4fWt1;4I'
    '8)PV>VP^|tPIRu-h#IY`-'
    'p<Jnm@GA!Egjpvkiyg2DmT&kp>?czW{Y+WpbUL*`;CCXstFRh|E?HQx?;IhELUb&XbOG;zHqr5i%enH(1Qe7+>PH@2wiKl4UlCtISw>T=4?Qbo'
    '|xPZtuUrUnGbrMSJhYvBH#~4_GU{DIE!$I0xjRtsv_f6=PI%+b|tLMW2kZ%bwiY)l2B1^M1XA3L@X+kSxvGzv9oGV^ab}WS3#!7Ibk_gRLF)bW'
    'o!Ch$+xVN$71B79T<PaJ)_P3R-'
    '@CSc#B0yWWI`uR6gLURKc^$HY!MZcAA)QElNI#t0@FlMjln87J8MGStr>TsXLai547E=FKTF7&=HA_k2PjSo6)hEwKQi~45`WPbxWq|us7@mg?'
    '81pF*VqjLPCL2Ej>sp9KSTjtYC3yP{53By7@tOdo-Er6Yw0x_5!kAIjmWG0}8j@9WNqMX>MLsdPULU+_2w_MpAOX&#~a(A#iyK;M)}~@$iqMqp'
    'NTrJ%56Tiw>PxVIm%p&Wruw1!V2V5K~Hum|{S0vBqp+QEY_@C@{k+9?virl`V>tBJc#B9LS-'
    '6bG^RQSz>**U@@xrrfwa!y_4zIGuQ!&uQa*MqABJk=|hl+3e#-'
    '3L{)TaS5+>4VCuAbN99rs554|)o(*&~4u|7dcU0|lPGGoT0@Fy*F14%emW@P|fkaen!8<}Is#d&el<>Bw6Q2>)pc^?XJ}bn{r^0S?yNeDKLeHl'
    'Bs)+WUiJ>gOG~A`;Ap2eJZ;u!B%oWHpSK-_$C>ri7MuxFh#O`6gJ961qMv6ugi+e=M@`2UJU<AVyq}{+Tx`n_k`!39?l-'
    ')JPQTp*czg6&b6>^>`pm(>BsKMn3pQ*tpUiigWH7j_ER?WUx1SbY#sB{Y;3(AFN*<0-'
    '+T8%H)G3L}RcBq>UlDEF^x+tE)&kKwzX&vQ9+YO_uykV^h5++myBFahB-L-TltX*MPYqStUqER%~tf=$JcMy~Bssu|$rh#g);IfI%yK(A@aSRP'
    '#mUtwqp{p7tBA;Tbdd06+X9)!rI8iOo4mC<P!#ui<cOtPPL8(}5R!xy5kmffLnH7eO5H&^G+EFybw1UyeRCGp!Sr<I&Zenpb>Mb0KU$)qp1mJq'
    'BNe6FoAcrZU36o!GaGW^HnDk)~yZr<`px#kh@R?wDKsAh0)T6M?LzEEEtW>Hs`ySQF5*W1}XG={rhhscmqt!Id88C!m?5sU&VUWE4WH98Zu-'
    ')`5eNcNRPt(g`WSb$)qln3<!s4MEij#;LbPG21y4{Jo%<jWr#N&?)Xkh+9vBfpm;^s^w1Ib$#FDh~{wqY*+!lUjvSQZt(ffo~H)%w|vN><=WAq'
    'ajcC=^0Pe7Cs+%=lh$aE!bwvu4Mv&z(IpqBSe6TDjfSSt$M=g2JgNYWoNTO2@B_FAt(MN(p&g5=u{1z*oa2qF62|R0<u1cbM;taxyhR@~&c8j5'
    'o`C4NRo0GZ8gJfk%B1onxU|69b-'
    'f^N7M|x%WiV@Ph9kY?9fSlo>hsO>{7&EU!{4hGoS@6;$H)(XL@}9iMnwwnz~gXdG^s^HT#DY6<bg^Z*5oLR6CeuU0K8wT(!=f+xo6qq$N&rRuD'
    'iVe2G-'
    '`0);g#YUl7(VFKQo%9e#o=1YoCq>L6DJL>d0$cceIhoZGlnk)cCo$9nBZ{nvBUnm6%lXUXV2j^w45RP@pl8n(zohJ1B^8tlUePOs8sPKLY3w@b'
    'ja~qFigu1GS!=+QiZqXOP%G3>S(Fp7d7_n{6HyC_RM{vsi>;d0*ybOzWHYGm<SEx~B7I~vkE|vP>$+W3ff8}sp6>=F&jpd*&HLFTCrGvms-'
    '_DwMO9Z1Hn4g*{TWEYXFN-LOt^ter@7YAAO+W&wN^DMTC{I{8tgo@WCLojXdGnKvLk70=Y2Y}(;rlK>?ywh47ix`K2LOrJ5V!ZbdFjKOJT*+lP'
    'b3Qt*DF44#*6Qsj(y95_D#6rS#f1fHTxcsXw!gA+;dDlTIJ<Z>F<uSN?J`d8}g7-DQ{LiaU;FOHJ-'
    '56!j!0N)Jtfcwid4$xfq8f<jAV_@)%g=%a2OvBeyyl68x8rehn!jJarT*JA8;Ehe_kqHr65U4HVNg#FxbY?YK3FpV`1=}Cd!<a*~sim0$#RSwi'
    '!T`<Jbn4$2D8hNNN&uEB?BXB<-'
    '4m<5O1NJfdtUE2s?P|NBnBB_^{8?L~Br4LG!78eSI}xoC*kTx@Er`5rdh81Fy@E{0@~fDTRW1q}6ra)<1z$xP?}md>R2Lsq<sw#ksze<OYlPmT'
    'Gv0KK2d&s1?F(b(oD`yjJ<=FL-}_n{)Wt-;sx7BeC}u67WbH(+^>$|{1c1aM)E`BDL*-'
    'G^WRmDJKLn84+KK?0T9Z`UH&dj`=G(2*w_(MNc47rXMS{V7*LOKFxz_x2G~*Rp7LDfPS)CEoSuA;p$XVVy*~jhNy%JWdwZ_bB*oq1v7~(y{Z?{'
    ';eao{Oka@9M*8tf?_t9AjgT&NU;Eg;VFF~$&DzLtP!cZ#-'
    '}KpWZyWvJSyN}?>moRB{<+4q4f15h+0#@<Jx?O~|$cMN(l4EA2ruLM<H@Q^Pq%>MJ$5;>dwk_g=OQZj2~-'
    '<V!)A2kk)YLuHnE0|p>p;AghRlER-uRX5(Qr7#x1x#!K`=A<?waxTPL8%bhL<ZHjXZEe}{y11JC|E<T5--or!t)JBin&3ok7T}Mih>-$a-'
    '*cAX}IGN7%9SuJV($|sGtWIGLzZ8yx}q2M)?|pI(~4~G@z3`1LM<Wp|ZtAr?0N67*vXk!iet3R%;9ODH#HADfw1HEiG78HE#yB(##=7=SnnaH8'
    'wgb8InP*8lu?OjlxzArV@20y1VRTX-Gy4THL!Kwh|h|zpf{|vdZ>VWZM&IBW0UmSa#>++uOh#sUP-w-CxQ1Y73N{K<W)AhIGX@m?8;>5ltP$yK'
    'x6}!Q+^ARl`S;?CZwb<fKk+pQXO6YV=IVOU(vkxIw)tI%}#Wwi<>ST`Ji8dDL6~LW+>#H)@4)m@s#%X|S@3yr|)zn|qN`J#*&oiBPq}Hxw_P#k'
    'Wn`!Y);YIEHImBT>vEOFbkxleGBa?<rh|GFl30T8I`akZ?RxNsCF+0pX=bc(Fi+1&V~2&dvlNpD<D<5v)v$U}^1&;m=4r*96!&EgQtSpju^pgn'
    'GKP5&`9l@Eh?~*^=67a*6oR@>q<?F~;D|1xuUcS`vZo#S*0(5Uesc0DvoZQHXgLD=bCXh_V*-!8A#Wy?Tta>57q-'
    'RV0QcToQ@O3CWPHw5EDx0xeB33ajKrQr}dI0>p01u<6M)QQ&`ywKuGRJXy7gk20vY=q2R=**D8W6{(%52sRe9dI*KNqV$GF44dpwNXGbz`L`Rb'
    'R=iZ!>2b~P3xt6d6Rxfx)jtq~g-TI6Yigyi*r?66OICIt$&dR0?Xgdy-MJLCL`Dz|#v)$mqe$<l>cp4|-'
    'BqpG8z}NRek~<QOtZP5K2$<Vf6DXxav>;`=IB{U)PW^fX4M*~?^B?@>d>b+f7*onXtRG&`Z0Z_1L9tf{LNO>>V(TNi25E%x!K9A%3?*cvKXszA'
    '#Af+oe9S*K*hLbTvtH=jhUno*PqaGEYwV5CrFwijZ|Y9Ou0Y|2@jK0L@yuH-FGd!RQ1><*$VB5lox~k>%d5ICo5pm9>ZZXfQ)PL6g?XYRzV9bd'
    '1$_MPWi1up;QS<tLoBIGD%Vb3=IvK_P)y3LA*pG1D28?oc}C#@bZjGjH#5%vLXXJ`ZPf&t=L8UJ};*b!!3fWTSC;#szP<K5>sMc5Kq+PNYwtrG'
    'Je&ai*AM01ruQEDlv<$1VUjU9JwM|(iO^+t4V+rZVNV`K7Hw_sYcw3uSD<9=tU1?w+5<nUxpH5=^DDTtH`LXY0gO<T**>1UqKpBFhZqG*jfyg1'
    'CGkNhiT@9#Jc;$s3YJdO^6Anj~&r;At+7mDKVKxYrNj->}Xcyr0S@o4eIKWk)g-'
    '1fGBr~2sbkStc{+Pf&|f534Vb=eiB29#gxK^O8tcSbqz}<`l^WP#cAQ3&`LgBmA{yECj6RS0V0tXQqi+gCp>dFP8`;pNNN%*Wu<a*trfh96Y1?'
    '`VstuaVRl|Rv#Tt?%LtH64yGrW3geL#PVlT}hCsVEV@?prXb>5^DQlitLnL+S&5X?xyXe&7kT?5#>EUp(u2r=Z<uikC6i}_s5GQ=W7mF4P@Qf3'
    'Q4NHqOvY3k)cUpj)7{r9j@AKt=ILDx7G7{aaY{^nmihVic7?#9kFpS#Ka0I{u@Eo;rTYVl9fnT!|Yhh(t>SGf{ltpCu9!m!edt>PR^a?LpeR_o'
    '#F~=&!Sj&26!(pY#GhW7F;7=dXkCkI4inYvmxE*C2>S8UEi22Q|pXSPAr?r;pH2W;EFXLbt^e6k5pg+`si}3%@bP$d=9ccG_$?=0tzxcdga7x{'
    'ZQ^~=986r9tV3g+e5MA0&vEt|KX^zhn6npsyDOEEZtYt{%(;oi>Q~~+C4ZFXV!HvnRtiyKDgcB2|VAw?_-Yw=U4*d6=U(1&kop<n8n)ODv--'
    'uFX-RumTKt!7G*oX0(m)YOpTBfFTzu?AKa2|3e3Uq|k=l#GbG)oTtADkwN+3Zmcp5)}SlZ;oIweE{yw;PR97LKUvz_UWefi;&i0?ct90?z#+>;'
    '!A`9c+b%TTyn(uNF7`U?+IqFM}$(8Jw)|6iAt|8-'
    'S$qVK;C}n|@)(51tL)eBLiPwasF;;1qX?o4LxHC!5_2fK`C6%wexeuqQW#bhKmbxC+qK@2b;OdJqoh?Pw9eyBp*xaOT~>sURQ}01$S{&lcXqFJ'
    '%T5er+e%@`D@#MunPeRULqshlYp+X~YPGsc7C>5Qt$dFy$hwrHpIyb`Y-'
    '1ulnBeH7D?PV4>xm$}wiGPfr`F={Z3A=|A#=I7Rv|`I)yl@u;brvWWuFyj=lO7IdqCBxRUzIahRQxhk;jTrn5qs<{&U=lidg-+cHzsUl-'
    '3;97I#?|iLzVaa$tFbCeNMfwAWj(}R~7IV1$Ksa)hlaR7wv+5aZfYIl|aM=kqt6g9`JAUceG7vdvuv6YF0r&#5s^FjU=E4A6{%Z*usGXmLWj`#'
    '80Wbspc44TK^>uu{gjTQla92inE0R1xf2;8KA*HGrbL#Zk{r?*R6YRe4@09UxC12Xid;UrKtes%Rm~Q}@_#(s(#REiruS+6bu0-'
    'dt11zh&lPf$t-'
    'lt&53g{yIlBH<qG`pZIu4NQcG0d{n*%3dW&Bak`qr=akvkB_cTISSde+xE~w?rQm*Jns2mbW6g4&DpoOuwGq#VdcN_m8d}y|0g=c*ao60o@JfN'
    'q^G6tUw3JUdT&^osd;UTv3FI8GS!Z{<HOG&c1N|>8GA`o_X;l=gceTUxeT3Iq!5OTtAJ~t9i%pF+(RzAJipIZyddi7bW4c;NN`*?@59czOQbRu'
    '%=|zr=QXNOSkwvNbk`=YCAM9LbKn(M%{7fI;XFuhj=a0bpPn8-a5AL@)z*VraRE{-'
    'J=iiTBV~adV6m9g~orNo1*ZNDq{k|xBzWFW;amXf!TgNJ=B}E!#AMCNAS}FT+Y$kyq^`=9_>IBgFEd9f6Ol)pju_L?HRcyX6}UEzraPq7X1?Ea'
    'Cdq@yGnOqIjBsppWYrt;;mQ}Ug6+P)8WJLL4{L*9VC8x62BOSc@=i>%F%mlU~!bJQFIBQt`)({?XWu{ZQL>sqQdbs*c>ESv40sl;k{yEr-'
    '#M?X8jN|MFSn1CE=G19l0-p{l?HjwBT3LWUNoIY;Hy%kTd<`iLdO^ZX{zc;^4-'
    '?mpgce7sJp^e|>sgx!mi3y89My5wmnPJ;<MK4A)ObTkGn~j^3mD#TX5_kJHMZUV%2Sk3JAoiTqIu;r25mGC08W8@#vdHW3~|r28=ZJ4e@m8XXc'
    '+T_MC`SgT!Lb|CI<!&h*obh+9g-F}Aj>kfY~y+yEj^#0Mid519Y8^G-'
    'Mrr$aYF9ez=@Ytb`^R8KQ1P(sjRc|y^=ouEak5l`cRsyTU?OqvZ(52Q`&)7+g1&3kRKPPB;`{-'
    'TRJb||`1}zb3(!w~Kq?yKmlvR{Lu(}N}N#h}^KCsZ$1b>Jv-'
    ';&ALrp1g?Vp`7h4@fL=IeQ4JbUKGbV%4q3?S*zXVM1@m2+)!IRT$b4`#Q%N{RW-'
    '?ef?U&Lp;el1XT#P#2db|5kHTi6_({Z89b?TT>HK<=ZH?NVxL6D@>*OG-XOyt!_FdAxX&mMz!R>WlcuY<&w#H0%(&AEm`x8d$^KQDCiyG5%`);'
    'H!zW*P`Rof%zx=YZg2?yD^mo%6&Z)mUm-'
    'B*ZC1w6tULC;k_e5|I{_YcQ0xZ&}4@}ar=luCL5(~l;IK{ub^N|B@LlgM%CPI#~$0`MvRoOF^=Q>%(ssDa@BRBnmuj04UU!@97s)tJ7KjEN~T!'
    'thh;LO+HbnYQxMc5-'
    '?<S@@fC?;u1zT5BhGwa`X3MI$$yjTuPu25DaN8v&xn)|7fr;62?<Rd!vSO}ET#5I6t6<`#x5C@q48^}h#ntldaI1rfMIEC2*vy$4zdGvc3O<YZ'
    'TzCNdKR)$*;DmcnRCO`{TjeJAv4=BY0&iwZDA3oC|a1J)h%G?%gVuFR`DLJSuKVf!XiloG>=`r;e^RV}ig`WXY`8})W!pkWW=VhNIPkI;l;8iB'
    'dCGnHVEppqiiH?BjV^D!;80FUlp+uACy>tAXbFiRx%Jy-'
    'i{K@w3DOT%r?jHVemRNKfl@!>~2Mm*rwQb1NKn#N}_gQy;h0UYl;wihwjQA(pytCx+o4a?vBk(#P%sU{;k5a@{CPe_G-'
    '9P%^n49(y2UX<wmRD1{iQ@=t%$YI&MFazNlLTG;2v+xjN>O2vHyw#x_weH#HeEqzQNrh(<OX7<#zRop1%&)JAX$Hyeqk!*$$z=#1Ui(ib+V$@7'
    'S$;ZH&D0(m$R8N`%@CYQ9eE-&{s7ask5Nib(;h)#`yT!%t`PNhQ$crV14=<q)mWPUlAz+!4g%ID={5I!FFId;spjX$;AM1P*H=J-'
    'hv|K11_7~J@Hruat#t3h#zyT*z74|DgP!^<5(*|^*FYxnCEN=GJ1GVCPiWPe3bh>h3)=1DOsjU!FAeToofUnjtU+59yd_zkq%4r4HZ_>72f5Da'
    'r8673}~_fz3_d32V99nd5~0N0x`1YpjHiETnEnoDsI_*80s6QGTx+#f}{-'
    'Ul?sqY*YF;1&eT9bB9fh^b2B{+Nz#Fv(1K%KT_N>28rN1C((e<MQySl-'
    'S^QGdMwtqaaDAKf@1qZ}&sc|wSuqTR`V8%o4gR#yBveu{=LikS+Rr@kKfJ6%0<XwT0{bV^{|1=<B^>y#KvuW`pFf@c&*>))9Ln$D(I2S6bv}X3'
    '!uq*0KVoph<1^&dU)4q%RDiq`tDr4IFY6K9HgO#Fc11@x`UP<d(%h3K5>(-#$9-'
    'a)w;d7&O|g*C4I$MWeJDu@3hglV&vASN>4g3tSMbi*pJx`<AY;+%4lUq77#+xfaR=>5jCLl@_n2c{kNJnNjW7rzB12GnPZ|$zKKyvUCB^hA5r?'
    '}3<**L42Hi#UBP-JfvqVaL=sqcKOicfSg7xa@X}F`{R4mDdagRJC$YQu@h2t>CDnLR*zzkjKwwZ9w5&kS_x)GLhhL5umlh@i$L(Uu158*#V%0B'
    '>7-'
    'aw@MBOEkh>ZhOyU8kQuqHouypTsEo)EUs@&pc;C(_)A@`4%)qi##GI;?|uQO*Kx)jgJNuOcK)%9A?Bjgr+x%asMLjabHk4py{B8!hnZlF8Tn(B'
    's(4pyXrec5$+0-'
    '_*X#KnQ}feb*kpPhsPr32f0mq^e(rQz&iKkM$1)y_Za)?*%#=X@YMDRdH0c|GSpoVSAWk$cs!lA1uH&4dDlkC@0}b^1)|Ky)u$v%{T1+)#W<#+'
    '>t}$CUy$YGBiQWg4t@9oJp4Uj@^#>+pG^PNp>`kRdHinr@6$iUXnXegb1%Mh-iEc!R;^ep*_bQR_uC{-'
    'l1L?F5;CKqigYU}WzugPrG5^_bd3vcdv#rx-E-'
    '+pRbX`u#m!;jkH%j9iv099Vxb_Q#w$c=H34o9k1jJznRiW<_Tfikpd4>5+w5yJ03fTYD1!?j=4Ym(<`&WACxa(*Dr}q_BRML}N651RXHJNZiIp'
    'm$&ly7xzhU^3P-1`sBpVApU`okHv3H5d6zI<Q1&J;D`B;l(s^QT;!((zi(3<wG>dw)7r0?^F=-'
    '1cXK1du<+W!R+M^%+&)`27zF<m4@_SZtZ#gU_2Zn3xGl@FQq$2Ci+kPjAY&goKW>owa?EFB^CDHO`ypRFd>gb5?5>rym;P<2^oz-&!dNl-eO3L'
    'GF&;n4^GLMmr62qD&kr2*$qcxn`}#qbUw0Nzq<D4N)GQzyy$v5GAHUt%7pPYD+*iVTQ&s^^qX`8Ja<xKJMJSwPvYfXsD^`XN1w6Zfx>fgHWVl?'
    'bL`Js{~G08|CY(CU&*hA<!!y-'
    'ipsoRpfj&kdi>@#uqk{5<2v^x8y&<dYmaVLV^(+#<6zeIU#+hfG~k%rVdecmE^6aI}EXhQ3Eq;eM(q!R4YAvkoZ74?8U3gX{+w40OnN3(3}WPJ'
    '6KwmV*DY))pvhvr3n56NFq<7WV}$;6QkF@rd}UTwQ|$t=mm<zXM$=;HvFS*ru-pDlpeDN&B#iU!P!E1!Y-^g9p*nFxH7h5y8bd-'
    'V~6JCZ)Fto^SCV_O#P>D8S|`5@u8E3E%3*p+j1x8R&3=<rS6XDUl*}`AV+wGmf52(=z3=eNKe-'
    '9Wv)4oZTb!j_^&DE?^~O0)@l<0tD6HqMSiPbD84=3o5B#ND9X_1=kh3B87{@u=p#BWll(UB$w_9n}(2Puc=xo8LNfKU52DF6;294I&4x90d)T}'
    'vLPZP=liKy-fZ?adCN+Qa6?g_l6Gl=%I6H%1x$*uNnW|4{-#;IW8nmKi(7d1xJCwoeA)~^Z!;p!HiEAjpS-'
    'J@7@3*ncDzMgpl6n<d$han(hzqTuTc$|+6g4*ZGa)OyB#nh#|Q|+9a<s<Dd7g>o$2pjN?$9s_#~9-'
    'E2LnkeFjbk97jGt7$KJo@NcsA{hTB1JvTmI8WHzL7^q2qy&}eq^$W3qk{c?Jiz3=Fgc((wMtMdJUi@y1_XQ-'
    '0*F}H`sdHD!u)~+70F)}ie8J5CSGbf5%ZFVu<k)!zdk{fghYOc@+Dvfdkyl2n7h@lB#FvA8;Q@0q5JBEmfx0}fED_qtz}R5R4wHX$j>chw+bWb'
    'GCA2Wd5xU&Gc%OtGr0B#ypfRd~AI7{a0pIvgm+Nn)N$+vWekS>YNVLt6NdPvQg}4#V#>he=ZiDOq5=O}3`VlTq#z`SXyC<zQgg6{Ya9{EibR*7'
    '1UjfMrE=Mos5WEsQBs5YeuG7iLXj8iDflG!mc8y&@V==*|8-3%@(PMWkjjLMcvqBsnVlZJD(ifr-'
    '%;WU!uuFQ3AuvFgGgE=g+%_nbD?Q5Age;NyZRqSDAv0ujRSIY(=}{BJ;WtX><_jQ0Mx%d;(X-J`6OH8#zl3J}G`sbs-'
    '5<)|bix&12a{R<%kO_JVz)?{rFU&|$Fb%k41#HMQVfRk=Os1g?`Ce?Hj*~A*mN>~W<p8VCT6i5C~5pg90cX2X;T>XDcu@<!Nm0TxPKrvh^saxI'
    'W{kdi)-'
    'XPobC^Z3sM9JE}_#4DO#V0|D9f84a|m(&S>*Ogpsu$Lern4LkmrN_Qn_b!w7r*ccOJ<sQWERz58g+w!af?5BmdL;wR*&I79(6Zo9%(VhbioZq~'
    'Si!4%UkIY~hh`%B^zEXM%*P3{kS$(R(S`e)W(K7R%e)IRYIptj@9%=+KH^x}U#|7=>T0Y=cX;Q+eMz4T)0K41~6!LWnz{7=7d{^^&_y>#~Fr%$'
    '*Oo!(BrL)jDQnk7mpnr8fcxjhVHD3OSF#L=g>z14v2!f3FyjPH3Kd<-wGWlA3X4-'
    '<f*0e#JgbrsnU)Fs}eu$E~>&CV8~`yxweUwSDd6!=_aj66t$Id7f6T)n?yn>~NmI{A3!V%A>Xm$R;>O_>J_{oa&vZ;~tfU1oZeEF1oy0Q>Fqeo'
    'jo*2qj7^o=v>dd&aUAo!-lv;gBW89Fjzw&P(A(MznZ;^yYKSPl6>(q#-c5YhoC_Z**UjJafKpzH-'
    '`f*YF|VB8FShaO+tL90WMTx!tKd#gap2e2gFX^KAt^b!S`Msko&_=WUj@Js`$x0Tw+IMMT&XUq9>x3C53FR;#>agOhl@HZTcdi1?6nFP^*NGM('
    'y{5dO)S$YI4AOJ+(6tTu_kcQ(aVa`z-^N{q_hQzS^KEAc7Z<Qtrba5>~w!EfkQX6-'
    '@;teCT^c&f*AAoXQb{Sq=dG<;uR#Vw&{avR${=|0m_qE!2(NW>!Mg>o0(fSS>THPn{AVi{k|q-'
    'oD@GIy01=&{NC;#w}@&mhS^Z3iuSTv7`Fh(iDu${2hU0>Z!+b1p9J;*tsH7%vNnalK%exXkEjb466SC!@s5C-'
    '}fD`=HRr;!t{Js*TQuL&5Y6$#I}_Lt-'
    '~*h0uKvxD!C0<y>b?SzeQ+ACSD^NxIgqn}&YI4is+YEORtKuR52T0FtxPPm;_GQ2E_UH0>)Nn@Iw*X2s82k1`^3pE)AXpQk91=%mB(049+&N1D'
    '5k2~kUbA45Op&!c_mMAJ~f+oJQ&Vo&oX1j^%yX2eY%f95f14`iZ}q;pouc@A8V9&n=hOmC1~jQJE{59&IgKCWQh{CNOn;fQUSg&nK-'
    '6<!NjNC&Zf^iMp@lf_Z0uA;-'
    'bVg$Wq#?u~14+{mEO3mJ47?(*&KPR*QeTsMZ6l9w(T!*+2$^y4j%;elKz7pHZ(RRe73}i*{+Rr$7P;K4^!aVv@3!jtLUJ8#TV<=blIclW~(}_4'
    '@(G_>a$F?!X843QdtuO;$i+xTqF31u#ILo3H=Sy0-E8Y*qph%Pk`1|dCEFKHiY6TNnOdyVz_yW%xO^*!IHEt-'
    'F@uCh&%>{U0iWLv(p;Z4J#JHs2=EkxaZrKw3R9D6wo9$EN>)z3+8yfr$b)-'
    'kD;S5>`G(l0X$(UbwlnKOsEHArSx*oJa5t+3r8m+j}O|7bKz+06(wUwf9Q#;?|&B}4Jypxoq!^>La>^#Qf@Vq1@YJ8)JhumMGn56S_0sxt7_JH'
    'VRtbA!v>I{5z*#@IQ2$}BU2Q3-^M*LC@fs~q?@B`CyRVVYFMl_@>tz{9B--An!bYR@`!UNca`S<-'
    'eDp~jS914F5c5qjc%mWHX7|eHa$npt<?r|}N@5aGVWLc?tS%%n=@kgtBmIA&}bN}$@3WZ<@XM>i`Vy2BN848~g0LZKZ4r=%L!Cgh>KngK;?vqa'
    'heM~}>m5z=FoT@$$WgVn@3K92!xt)mYXiAgA{hUW{8#(r>FGDg!>L1R`iRI9gq;1t3Xi&V=@B^)CZ!+~jE6tg)zd0ixl2s0~Wm}<E^eOsh2+0p'
    '9j{Y9=EQ%A1os#dxk<Iarrv`1<Y9t^9dcv7r7jf<AD~+=|)VK&s&dB`A3AdOd3TeSUgVDPbhPFrNfF7?e;5(NhfZp(N1(x4(wTd7JH;mGJMb0p'
    'aE|H->2f{YQb04PPkTY*!@@nmJMT0floDp9L%4(@T;HbquvAB|~f>_SX<)Vf@ofe$?kf4^HdaJtLwCWNp08k?n3aEXFq|#vlSW4i65(UkIV-'
    'f+RPdJO@KqYcnzQu4cBxScHeX#}Xv#<za3EX_SAJfDG1YgD-'
    '1ZVg_4Fo=nVMocX%BfbLhXW<%0Q^YsOqOv0`sIIq_`!0GY0&dIO9)f5Cz<H4#P=zX^BZ!pTqE)?Qzf)O16gZ@1-'
    'k5^ZbHW<V|&QZhllqSgBcu3i)6?<dhRY06u;(l>Nc|y8l(y<#h}n7LOkMV6j#LBv)^VCzy~Z-'
    '&=6Eafa}8%AqsUS?sk<yxQH=KxJmyXfGDb(m<CfHYa#r!v0oD;J%9~<k7>Vz;s+A0KH(wBxDOcoZN`i8YC=Nr)4b%!Tv)WuO{y03fGL48z(*9%'
    'a$|AmmLw{-H6Y+LClSi#a^j>WlHDZ&d%y-'
    'Ga=FLDh7RHsatbNA!{i`j<iPMiZ)M;Vnkt?hvMiCQcL*VfwlhgPu4k665}p*IQe)lc$=9NS88d*2a%QuoYwdo7lL_7>6uf24G>h?H6~jN2Bxqk'
    'NG=;Q+3*gs)kl@dH7FaBD|A}z<J*Mbh<G@5oC*(UIqt!P&sZ{t6J~J7ln-Z{jpr;Vtw}f$`)@-q&#Quf*rYwpH2C>A<oJ0ElGs`;V-'
    '6|=l+%{i#G}kb_@zVb%4)nBm3FVS)SS7ou*Z^64hQCoI`P1Vee&kX;Y49?A`t%C?fIo82IsYbH<m_vlpCE5%&Y)+U%-'
    'OdrmBwU0s$U!*t>9Ev#I&fuJ)2!C-5Nh`(eJ^dmXFq%X)T4*{1!p|0RgJ4%)r{wr1V*kCUcj<gz-'
    '$D`G=fP0`RDkGxEvxIb%+K+}4wA)q!IpxGrGC6|77HIQJ9%CZ)Ds9GLfjvKH>KGzL0*Myg}KCZ9N=(90~6f~?i*^S|ZM6Y39^m9oa?hJ8yHPb('
    '1<@<(+ORNus`m@~fg&$v}VSdF;}_O5OQ;8BxtDr{oi&3+fD@LHxQZ%|NfWn}lf@r6ADM5NbDoB#BWT&&!qN_}>cD*-|AKp$ctop?-'
    'QFt=J>kpa(Y1mg@qoBqm(UZomrqU$f1sB=uDz~BX8BEj%ry<i>YsPg_1dsd_abw&D57y8*wWlr8Br!|botPn{|*p`+1*eOOM)uzl2;hJf9+~c+'
    'b7Cb6Q29?;8Og=Vfxiaqh8c!J#875k+C{J-_K?5SF)X|+bWO%VwrV`dW$<$pWU)-y@kIK-'
    '&aUFk7%(BrACUbsbyP33!X=NfPx#9{p&@oSwvV#dDBY8^{aY>DZX0=siv@#Dz$N7HEt<;LE@HWd!N>b7HxxAm^WTf*slp5lEcawB|XgMXQ{%JY'
    'C?@Kj<RWki4lgQbW^2{-Fz)V<b3RyggJZMd*LpI4=ZPrkZ2O?zTp8*QYN-svHM!H>ETnA(+h@{_jHmjhlnVQ{bm#WaCS4Ki)W?V^6ou+mvm0{B'
    '?)(NeM8*-$=!}1c*)}tf|eynB15V0mJu*{I)7GUNT(L*{Vvc>0*HpV^a3gEU0G82&9^;;HabeqWgFImEGok2K-'
    'm&X}r`>e!3ssmF^f^?nq$a|{}DRWllmm^73++lfOX?AYy`lw9GZ+JaZiZ)O82S|laCMokw&bcL8^qP#<)o4jQwu$s;OP!l!bkx3*=40wV_Pu?;'
    '%+!Km@8?saXcpQMeg#HiQ$7=6v+(zhv{`a-=<C#7`7b|uYURxH&!KsO$E6ADfMIvtlP+ztvXNAAPb9-?8;6f{%Fi6%53_2`P$-'
    'uCrKk*qTm0(T7t90KDk<A4R#EP{o>sHRykd+IiHcij=TSsumRin0fIEbkxA<Gmmsx?(?_$}yHA^h~-'
    '?%}VbR$s*P06{{x8ZZ$P0Ik)D5f;q|Ki$U-DG~Iw?tSsxT2IlN$R?^KT$-'
    'Hh&M>^9{t+ROd?=kTzr{onW+%#u^FgTKJyVe8nvxp<q%k<x4oGa&(ku$cu9mqk({nMBSmT#boYLYX53m$<=J?>2+r3;XPR3~6+Kn2#Pp6!AbgK'
    'fqI4TL@+XZCF&w(h(-;n=;qxTkZ_DA(CD5Z|71L%8Y}msqBrPd|8PXpm13$eOV``~$y}a&1#kECs_S;MXVI9YT3S@}A#Yzfj`kWfgOQM-kb9bT'
    '9KQzkWvA7qZ>MC^?q-j5PwEvvM!2LP3eB&!Id0L$o@)MUv(e7B-lSXu|OXVb#VX2&ZO6eml7>U7|B6@J}`$~i`8|kFCSXc>nztMwlm<&g??-'
    'lbo&%{$CHx|Yr%#nLB0>ZxxT=5!lqCdC?&%l>Va%UDw1_DJEcJMM!2fD3#cNiKyka^aRSt8xV>kbx?RlYL!4w@)3&Y&AMqs@M|6~TBi>*#<XsO'
    'yO2a8`;QsKfMD#u-L$Y<GrH3j^i5QE!7R@g;A;{Ek6198p9!FOJ3aByRKPIn>tm@HhE##JBX-Tn9=;au+FM_ZV?J`XFTi-ogvm#CvTp?T{39gi'
    'xTvE6(|-8*L23E&JT*B{6mOC3WVHSDbu44_*EZpz)AO06*lMckp&oc}WE^+$)Mw5fc+z#*}!O+o9L}zg+osNr{BK>F^3D9~`}78m-'
    'sM&^YiGZ5>eG3pX!ebJ&GN+cO^t79DaHd23DzmV;N)nt52`Xc&#g@+KXo^(z6tGNkF~y(es&t@I#fjaI71rIqS&X{9n3r{=*@Hs`DcGOcn}qm+'
    '@f38nm+@@o1jj=$O5?DiX0R|}Z|3T5|gnUiv-5!=FH6tX*&C>nMq39LH`@EX-nHK?IHZyB#ip0Q8GK^vh<sTCjgc#Nc3mMo80E@nQP<IV{Qrb|'
    ';e;Tdf=wmRdJ#{bS?xv}?NyD<W%*uRjG-'
    '0?;7lW{Js%alT$5CNW|=CH$*Now$|s5X;+F&B=g1^<4=>rNk%Li#|m__v|oUvQJjO%ZOY^M0x;CWPttTnAKPSC9J?#b3-'
    'C^GYmY!ensB#S&&NJ|G!=Un&2c>Io+ylmakdsB6~ieVC~D)zQC@8<K(rT<58mo+qxDA_?1r&>763XtSs)hIe(bOcT7cE1`nHQ>*&5sBgTA$o?m'
    ';IlafS7PM=@Vm0iyve-C<bR8-e!toq6u4yGNKjZfaDJJ-RGC?0ubSMJl+YU4O&5A+OGZmDIkw(F!lv;-'
    '=#xmN$gqaMVqJhBa529Xz4&bkEm=Qk4C1Z3Kc(UB6S-'
    'vI?!PNrh(!2`y6!2%oiSf}Bn(iWt;7RIXEG#59%U+(M)smsNci8!*hu#u}jkz%@6*pOd4{o8k&(m0L3DwwQ*CG?G3^KOGbE#2VDWwKu?4Faglw'
    'P4XuAxMVa>^YH92`yr3G%u*1r&(P+*QM@)s&!vG$ZpbrM4t%{M;jh!`G>mQn>>QH}hm*;_5YML}WHq7vwS6+|GVY4QB&L644=vE0mb;Dz)%n96'
    'orH6-v4#Vn~%ZW6k#F&T!c4rN$1drN)>oz$`Y#^&TCvZs{qlX|&$VffB{*95wPrxba>+`+}Qr+Zor5>`Qo6O-ug~5c_F-XTiKofNN@Tdr9rt<p'
    ')5d-'
    '&51J4(7N#r~4;>SEdfXL&dHb1jw>ZI+QZ2@<CjBX;v7h>iA!%V6+SzWt{Y98by*d<b>DYK!TY`pbk>&T$71K^Zm+#Q3)5h#c^x~mnru*D8Ar5p'
    '0cEiX6&v=;ZgpNqnR-T9x5U(t@-Z!;%mZsWi4N-'
    'd61Rp<)dpSfWc1@ptOo`(pJYSz$Fr)L`gU_AWK^!IY7)(^Q=HUFZ6f(5_$K9x9l#9l~eqU7MVoMTB$K7&flohEh%w)?WMKqTw1+5g2F@Y^1I5U'
    'IgH&G$#7|ko>s$wZI@D>SS#8mYQ~#amuSv3Q7-g90ICJ&=eI-PDc!MaID&;RVU{XLoB%98QoRFv#4A~(&9_d%Z?f;GvrAlE$*XazE|Vk!z8cp&'
    ')S?8)MxXF(>2+3}IQ~jAvLzKgSIx8DGdcb(@-'
    'Sm)f{3e+?am6Pq6yw2w*L)X`fxzgk(xPC3r>55`$BQkbAbTiX4R2;Zk*w1l>Ol29N08X3K2;PBJbxHxkGD(?jt_Us-'
    'Vc@7d264hFP;#S`5jITf+a--~Bx>*44r4VSoewJqBcPqmEtAI&Pwzc_s1JBFtZ=G;wCCl_E{Ci0O9|Yo%#Ua=)3O_}b2$-=mtm-aMr}<{^yiSE'
    'OrKJccuy$Xg6&Hxu{u9q;mVBU&?Q@td^|zf~PW@=}on_91x#yAhK;=SFvHcEUs4F)wQcq<GoGd6y5ebvF9IR<;Cs|M`D7fftk=j-'
    'Po)6T7dP{DR91EIVw^sI+uj=<<x5r{(IArla18ih0fC2~|_tji63amg1n!LrTp5l;?`ket#&)vc~*5JG-jZz+sUnAJBsC*n=wAUg>ukj{6~&ZW'
    '#8vtUlg&Tb8lx?4T2?-'
    '|dVeQ4%PmtFaSTl0I^J)EssO<Ml_D+uJ>&_RHDH5*nL<GIpBdrPW8^q(@_i$`+2+COmzjK0&uveMwECSaOHqII0)iR(N?-_e(A-'
    '(o&yL^}f1KCFxvNrmtS5F937(GJT56?bWG5-'
    'R`bSDIIbknb^UHspLy+pkiX6k~)x2UumSOIZ}y_L}?y!BwMlvAGDee*q|lvp$BDoB63tETZ9khdu*)oLyxs9PH{AVg|^msKY{E5_7dOs)pzqH`'
    'Pv(!H2|aaR=>H8wb}9;(fH|Zgdd;0e73dRX=UBs+VW1=bwLj8Hp1qGH7~oiKIukdXJ_pNs^5k`XIF>Oczf7$*rR-B^h~D*P`bR6ePX9B-'
    'j&0)x5jHbYwNw}qI0%4?&jHB=&=vS%S*%U+)J-4xs$E%QfF&>>zN_*t^BaF(HW2G-flMEW-Xr&$D4V8-'
    '(CyG$x49UZeZs>{{94pfgg6UYT=K?uTghxLLgs%V+2Ftr=_fmwJGTVet_@1Iu$+QpW!L1a!3!^M|{R>__3$_3p|gj-'
    'O(@cSN0n{WL09}0WaSx9&#p!^I+h?pEItul!bl70|0U{ejbagto63L-Bo-<^x!-?T-'
    'dWm1oAth&Hlyn`0Mf(@Pcq7%1+pZ^sw$CEggSd%C6#rJUYFeVmE}Z@fX++M5LbUjK=w})q+_;xA0E08-'
    '+t07xr^Go<w$4nb0U2ix$fOLq>1IXsf>yi4NTWAU?aROg|c*qfFT4i<_P1W_A*F^RSJ1UQKq5p02H};YKgL^_Kh!khio7ZTSu-'
    '+w&i6@375JzQUd--q;?r03@)6-m*G#_3=a@xoeE@z6Jx)r#xkuz5do)?0KGuBmw3cG{L{D1)cNusI^AW4>+>yx$I-'
    '7x6I3fy1iwbKLcF$S~iRDtG+~S7#xcx)OTE&Z4HKbtbK`|wxj4=bDVfThHI^l5n{m_8-'
    'e2l|9u6x1vP;;*YrbtA|ClMHXJstv*xU7+Ke|C1$+%R>UHHke!go-7|>qE89v6&0ZFvd0XywZZ(}V15>K!f*h4lle~C(mt-'
    '(wmXY+oXkNvppjZF?{*LdwUeNk?5s%~QF*I{3~K+%_<?1P*T_Of{vo3i={(F&ue;ZjyZXd3njAdvK7*Wn)klKm%^^u*Amy7(zDe*$(^Pd?iHF+'
    '5ZRrua9IPL|m8;zEWnF}j)g+4Ijox5g<p{R&ijR(Zo8vyS2uG*$@Bm*XF^tDFSmQ5Y@Z=@Zx*{$}e-'
    'f4TDU(ki3xmbUC6HD@2yH+U62bF0}w(mVXK`cho&&UjD43B4)5sqcykbu*X#INMFOU0QKk<2BfPg`F~d@R0^T`ePbRRG2kii|fsPpYhc^iZ;6o'
    'mY)6o<YkaXdmGC!>SciyP-MvRQhv#W|D!30`BSl8m_y7sSoLw($`OVeV76Fm$^Bjuhq9|GF%nJJEG>a+_J_-iR5!*wr{8v@fb_<8G`##Wp;v!+'
    'rrTX!dQB<Q@OqvVwO`6+C-'
    'A0amaN+Sl8e9Mi||sOmw4cO<OzXr1&Mn84}P#bL7~AQ6hdsU5DYFjB<RNOYsryc&jP=Sg$XVmu@gZVmPtp%fyVt;27_q$6uiBhb%8wqPjO>ta~'
    'au&hwyJ*rN}NpRNV?<Oc;)VN309`h~WaICYPa|Xy8h`a0$#^+AvoX|F0W_^@*i(XMVI)N5RNKW1m>!ZlAb?LG72AbCUg@AiyA$CAj{1($-'
    '_XFL*v7RGjk;@XVM$!!*j|wP5v7Oo)VhM$~wE@2u8L72wU!4g0g&g08?D#yP*U+Q(W2e~staCW(u{^HdyXqydPCg@7=3d?Eo09i6s{aH<*S$I7'
    '9I*sAj|wPj3LV$coW#0fRJ{l*%qB~QYK<=2+}al0M0+e_5ub$5c6`uY-nS%K+ydaIcAfw;RpZs)2?yC4WtH`~MR+AA+Tmu~_BjH4GDKLK(9-'
    '<Pp_(I#AzM1?iuiWkrb5U9gEnPZ?M_$cPRCg!{<U&Sohd<Zz%Ydy8u>9&?be7D){G%qaUCoWcJR}JYKXE%&?`WKYh!C+Yzm3dw89(KZR=go*pS'
    'V~adT9X7rsD3{d*B`#+9HXGKa16);`^O$e5a8h=d%&~!VTc0*?Rl=>47(ABB(5fAcmJ^muV^(U@Wm}ARl~2brHnmCdW4U^jAKLD4}xywf6@n0d'
    'dYd*S<1fk))KGG8rL~IdT$BepI;jpyG4m+D-'
    'V<sB$`)V{vo`VUS6L~qkU=DdFhoWS6J&WC`jNQ&smAfDH6X0RNTrdat`eU6<{~ZF*wWAHIe7tN3-$UDEI90m!A0t-'
    't3auii<nYQ255FVN9rF{M|C}*JXQ))E*j94VruCm{EEcf)RAjNUUqb3dyBPIf$M5b-Hr+*V7x$^vmfN)8E0rzn)%?+jCKpT7EkH2-'
    '^PZ^b0swduv5%QeK6ZKgHX~KN6Q1Pd~v6%IlVJG1sif%VL&JT6kBhv1=*At0c|5YpbbCbN?8o`}^sQ9K7-'
    '?nE(HRzhA=N|4lphxtVowpcOkx6j$X*nD4UY3#Y{=E8V9Q`86xR&56O{0W$kC(kspqy#}iX($9z+<E|snM#*&ablBWnCbP%-'
    'q|>HPKls6GOJ`p=_sV(TMK3@7+|y5;UwR$jq1oMT!F$Xi5^lTzq!%PR`Wm)cPwxN)M(HjB4F;8w!S;B`jrDzQN=dc^uF>0ww5GejJ04k7%3O+<'
    '0n*&sI*N3bQIH8Nxk&9NvH2t^{$*ET6TYX5tK<ae^iZu40xi>VgbM|xFlr9_-R{}mxc_P=y0|=PM4RDGr$4MOjkfxIkV#x%cg+j%mE@V-'
    '>~5CpA-d=@Z-1B&#b1^86xd%>maN-'
    'V)|SYgLUx_lma?`40uQtGsJ4<dGE}b`=8?6kx0<kLtof{=X$M&gR^vS<xgJ=sG{G%d?m8pDeOoKGO0HbsHrZXidaa!F+#S%woh9xX`zMw8{*%g'
    'h^W#eZz9zrdr~OB&^?FyoJZ+C*>1_(wxF63}WMNq+%7WmRTtvbMArXK6Vbl({yW?dcBk{~BGEef)LRQX$6tD$42+KyI7VKl90p|R$-'
    '|>_2Gr>OZ`mMLV$GX4|*fu*cmH|>L@Sj&<e_EaK<z->@-et2zxo}ODf<6RZe|`E#r1-'
    'zW;JzC`Y*i+59r((!pwQWq2|k9~u};PuTFx&2Ri=93Z)|}~Dzax$Q7c?MHo76wlkh2S21`j2o5;l=e*fY=h4Q~oA#Hl@jd)w;*r*-'
    'c;8!m1DP=%JqM&%O*N?R%6v@bycTE(<LUdW$<?POqzDUWwvck_hLPt2%>elZuhJGjZkMqD;OV)!WB%1_Wc7@;pd6jR;>pGM5C-'
    '#s#t=jQZBy#+d79vHsNt(*4fXNpxXm$`X$M1AToklk@h)ta5Au>s(_ZP{xB%c2E(JvWFbHP9AZ4);2!kwk8i(j7{GyLP9VQ~Iw4t+ukD8|aKVR'
    'MVE1b<UH14?>k3@Fe5q7Ecg4U<}OId0%9K(ci8DA_Z1nWOGqdSjQ3V&S`?!fV5|^>EITjFkwd246|qv_!LbS_`gviK4@n7-'
    'yX!J>)6UOcfg_<_jbT`a5S)?BFqiZH>2Yc0ndU(8`P0wk1Kbdq@PohmWk{gt-$bb7fu1>9%1O?eu+Z>)j~pU2yl13-'
    'rhgU`(8lijTtAKD$dy;aEax4h}@O0crlB)kk)-'
    '`0wcz;ii`X7%Q^s&Y(Z)pblPdcP>S()ghMKtOvp1(khFss0SW=elypBu`ktY@V`~`vTl%lt$wP|EC*3zmDlcRx7+aAuoVq+!?4xa9@Ty9X#gt('
    '#Hss*!6nD9Qs0+ypsfLMs(X$PBRD}B{y7yC3t^>MEUvcUFzXc$e#Cdqpt#_U!rllk-'
    'R!in)F|frpiCnQjqXu|#(i=M$RNRYeuJSTume=+3;u47x4P?({2#UN|Bw'
  ),
}
_static_dir = _asset_pathlib.Path(__file__).resolve().parent / "static"
_static_dir.mkdir(parents=True, exist_ok=True)
for _asset_name, _asset_chunks in _INLINE_STATIC_ASSETS.items():
    (_static_dir / _asset_name).write_bytes(
        _asset_zlib.decompress(_asset_base64.b85decode(''.join(_asset_chunks)))
    )
del _INLINE_STATIC_ASSETS

import hashlib, hmac, json, os, secrets, sqlite3, time, uuid, csv, io, pathlib
from datetime import datetime, timezone
from contextlib import contextmanager
from typing import Any
from fastapi import FastAPI, Request, Response, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

BASE = pathlib.Path(__file__).resolve().parent
DB_FILE = pathlib.Path(os.environ.get('JUPITER_DB', str(BASE / 'data' / 'jupiter.db')))
UPLOADS = BASE / 'uploads'
DB_FILE.parent.mkdir(parents=True, exist_ok=True)
UPLOADS.mkdir(parents=True, exist_ok=True)
app = FastAPI(title='Jupiter Fintech — B2B demo', version='1.0.0', docs_url='/api/docs')

@contextmanager
def db():
    conn = sqlite3.connect(DB_FILE, timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys=ON')
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def secret_hash(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(salt), 180_000).hex()

def seed():
    with db() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL,
          salt TEXT NOT NULL, name TEXT NOT NULL, company TEXT NOT NULL, role TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS sessions (
          token TEXT PRIMARY KEY, user_id INTEGER NOT NULL, expires INTEGER NOT NULL,
          FOREIGN KEY(user_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS deals (
          id INTEGER PRIMARY KEY, ref TEXT UNIQUE, owner_id INTEGER NOT NULL,
          company TEXT NOT NULL, created TEXT NOT NULL, updated TEXT NOT NULL,
          status TEXT NOT NULL, payload TEXT NOT NULL, quote TEXT NOT NULL,
          documents TEXT NOT NULL DEFAULT '{}', history TEXT NOT NULL DEFAULT '[]', notes TEXT NOT NULL DEFAULT '',
          FOREIGN KEY(owner_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS requests (
          id INTEGER PRIMARY KEY, owner_id INTEGER NOT NULL, created TEXT NOT NULL,
          type TEXT NOT NULL, message TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Новая',
          FOREIGN KEY(owner_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS attachments (
          id INTEGER PRIMARY KEY, deal_id INTEGER NOT NULL, filename TEXT NOT NULL,
          path TEXT NOT NULL, mime TEXT NOT NULL, size INTEGER NOT NULL, created TEXT NOT NULL,
          FOREIGN KEY(deal_id) REFERENCES deals(id)
        );
        ''')
        if not c.execute('SELECT COUNT(*) AS n FROM users').fetchone()['n']:
            for ident, mail, name, company, role in [
                (1,'admin@jupiter.demo','Александр Воронов','Jupiter Auto Finance','admin'),
                (2,'dealer@jupiter.demo','Мария Соколова','АвтоПрайм Москва','dealer'),
                (3,'partner@jupiter.demo','Дмитрий Козлов','Север Авто','dealer'),
            ]:
                salt=secrets.token_hex(16)
                # Never expose a shared administrator password on a public deployment.
                password = (os.environ.get('JUPITER_ADMIN_PASSWORD') or secrets.token_urlsafe(40)) if role == 'admin' else os.environ.get('JUPITER_DEMO_PASSWORD', 'Demo2026!')
                c.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?)', (ident,mail,secret_hash(password,salt),salt,name,company,role))
        if not c.execute('SELECT COUNT(*) AS n FROM deals').fetchone()['n']:
            seeds=[
              (2,'Volkswagen Tharu 300TSI','LSVYUAC12TN035029','Китай','START',14500,80,['PAY','IMPORT'],'В доставке',590400,3400,150000,120000,1500),
              (2,'Zeekr 9X Max','Тестовый VIN — уточняется','Китай','PRO',71050,80,['PAY','CAPITAL','IMPORT'],'На таможне',2785910,3201600,350000,250000,2000),
              (2,'Nissan Qashqai','SJNFBAJ12U9992210','Бишкек','GROWTH',27500,80,['PAY','CAPITAL'],'Ожидает оплаты',450000,3400,130000,100000,2000),
              (3,'Volkswagen Tayron L','LSVZF4B9TN069109','Китай','PRO',31200,80,['PAY','IMPORT'],'Подготовка',900000,850000,220000,160000,2000),
              (3,'Hyundai Tucson L','KM8J3CA40MU070211','Корея','ENTERPRISE',28400,80,['PAY'],'Завершена',670000,850000,190000,150000,2000),
              (2,'Mazda CX-5 Smart','JM3KFBDM3P0991124','Китай','GROWTH',19800,80,['IMPORT'],'Новая',560000,3400,170000,120000,2000),
            ]
            for i, (owner, model, vin, region, tier, amount, fx, services, status, duty, recycling, delivery, margin, engine) in enumerate(seeds, start=1):
                payload={'client': 'Демонстрационный заказчик', 'model':model,'vin':vin,'region':region,'tier':tier,
                         'amount':amount,'currency':'USD','fx':fx,'services':services,'fund_share':100 if 'CAPITAL' in services else 0,
                         'fund_days':45 if region=='Китай' else 15, 'finance_rate':7.5 if region=='Китай' else 3,
                         'foreign_delivery':70000,'domestic_delivery':delivery-70000,'duty':duty,'excise':0,'recycling':recycling,
                         'clearance':13541,'documents':85000,'insurance':15000,'import_vat':0,'dealer_margin':margin,
                         'retail_vat':0,'comment':'Демонстрационная сделка для знакомства с интерфейсом.'}
                q=calculate(payload)
                timestamp=now()
                c.execute('INSERT INTO deals (ref,owner_id,company,created,updated,status,payload,quote,documents,history) VALUES (?,?,?,?,?,?,?,?,?,?)',
                          (f'JP-26-{1030+i}', owner, 'АвтоПрайм Москва' if owner==2 else 'Север Авто', timestamp,timestamp,status,json.dumps(payload,ensure_ascii=False),json.dumps(q,ensure_ascii=False),'{}',json.dumps([{'at':timestamp,'text':'Заявка создана'}],ensure_ascii=False)))

TIERS={'START':{'fx':2,'bishkek':100000,'other':150000},'GROWTH':{'fx':1.5,'bishkek':80000,'other':115000},'PRO':{'fx':1,'bishkek':60000,'other':80000},'ENTERPRISE':{'fx':.5,'bishkek':40000,'other':50000}}
REGIONS={'Бишкек':{'days':15,'rate':3},'Китай':{'days':45,'rate':7.5},'Корея':{'days':50,'rate':8.2},'Европа':{'days':60,'rate':10}}
STATUSES=['Новая','Ожидает оплаты','Подготовка','В доставке','На таможне','Готов к выдаче','Завершена','Приостановлена']
DOC_LABELS=['Инвойс','Договор / заявка','Платёжное подтверждение','Транспортные документы','Декларация / таможня','СБКТС / ЭПТС']

def calculate(payload: dict) -> dict:
    """Indicative non-regulatory quote; customs and tax amounts are client-supplied."""
    tier=TIERS.get(str(payload.get('tier','START')), TIERS['START'])
    route=str(payload.get('region','Китай'))
    reg=REGIONS.get(route,REGIONS['Китай'])
    services=payload.get('services',[])
    if not isinstance(services,list): services=[]
    def num(key,default=0):
        try: return max(0,min(10**12,float(payload.get(key,default) or 0)))
        except (ValueError,TypeError): return default
    inv=num('amount')*num('fx',80)
    pay=round(inv*.02) if 'PAY' in services else 0
    forex=round(inv*tier['fx']/100) if 'PAY' in services else 0
    import_fee=tier['bishkek' if route=='Бишкек' else 'other'] if 'IMPORT' in services else 0
    fundbase=inv*num('fund_share',100)/100 if 'CAPITAL' in services else 0
    funddays=num('fund_days',reg['days'])
    rate=num('finance_rate',reg['rate'])
    capital=round(fundbase*rate/100*funddays/reg['days']) if reg['days'] else 0
    otherkeys=['foreign_delivery','domestic_delivery','duty','excise','recycling','clearance','documents','insurance','import_vat']
    other={k:round(num(k)) if 'IMPORT' in services else 0 for k in otherkeys}
    # Import VAT is shown as a cash-out item. It can be refundable to tax-paying importers.
    margin=round(num('dealer_margin'))
    sub=round(inv)+pay+forex+import_fee+capital+sum(other.values())
    vat=round((sub+margin)*num('retail_vat')/100)
    return {'invoice_rub':round(inv),'pay_fee':pay,'fx_margin':forex,'import_fee':import_fee,'capital_fee':capital,
       'capital_principal':round(fundbase),'costs':other,'dealer_margin':margin,'tax_at_retail':vat,
       'to_dealer':sub,'retail_total':sub+margin+vat,'jupiter_revenue':pay+forex+import_fee+capital,
       'fund_days':funddays,'rate':rate,'fx_rate_pct':tier['fx'] if 'PAY' in services else 0,'pay_rate_pct':2 if 'PAY' in services else 0,
       'disclaimer':'Предварительный расчёт. Таможенные платежи, утильсбор и НДС вводятся пользователем; требуют проверки по VIN и документам.'}

def serialize(row):
    d=dict(row)
    for key in ('payload','quote','documents','history'):
        if key in d: d[key]=json.loads(d[key])
    return d

def current_user(req:Request):
    token=req.cookies.get('jupiter_session')
    if not token: raise HTTPException(401,'Требуется вход')
    with db() as c:
        row=c.execute('SELECT u.id,u.email,u.name,u.company,u.role FROM users u JOIN sessions s ON s.user_id=u.id WHERE s.token=? AND s.expires>?',(token,int(time.time()))).fetchone()
    if not row: raise HTTPException(401,'Сеанс истёк')
    return dict(row)

def check_deal(c,ident,user):
    row=c.execute('SELECT * FROM deals WHERE id=?',(ident,)).fetchone()
    if not row or (user['role']!='admin' and row['owner_id']!=user['id']): raise HTTPException(404,'Сделка не найдена')
    return row

class LoginIn(BaseModel): email:str; password:str
class DealIn(BaseModel): payload:dict[str,Any]; status:str='Новая'; notes:str=''
class DealPatch(BaseModel): status:str|None=None; notes:str|None=None; documents:dict[str,bool]|None=None
class RequestIn(BaseModel): type:str; message:str=Field(min_length=4,max_length=4000)

@app.middleware('http')
async def security(req:Request,call_next):
    if os.environ.get('JUPITER_PUBLIC_DEMO')=='1' and req.method in ('POST','PATCH','PUT','DELETE') and req.url.path.startswith('/api/') and req.url.path not in ('/api/login','/api/logout','/api/quotes'):
        return Response('В публичном деморежиме изменение общих данных отключено',status_code=403)
    if req.method in ('POST','PATCH','PUT','DELETE') and req.url.path.startswith('/api/'):
        # Same-origin anti-CSRF guard for cookie-backed sessions.
        origin=req.headers.get('origin')
        if origin and origin != f'{req.url.scheme}://{req.headers.get("host")}':
            return Response('Origin denied',status_code=403)
    response=await call_next(req)
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['X-Frame-Options']='DENY'
    response.headers['Referrer-Policy']='same-origin'
    return response

@app.get('/api/health')
def health(): return {'ok':True,'mode':'demo','database':'sqlite'}
@app.post('/api/login')
def login(data:LoginIn,response:Response):
    with db() as c:
        row=c.execute('SELECT * FROM users WHERE email=?',(data.email.lower().strip(),)).fetchone()
        if not row or not hmac.compare_digest(secret_hash(data.password,row['salt']),row['password_hash']):
            raise HTTPException(401,'Неверный email или пароль')
        token=secrets.token_urlsafe(40)
        c.execute('INSERT INTO sessions VALUES (?,?,?)',(token,row['id'],int(time.time())+12*3600))
        response.set_cookie('jupiter_session',token,httponly=True,samesite='strict',secure=os.environ.get('JUPITER_HTTPS','1')=='1',max_age=12*3600)
        return {k:row[k] for k in ('id','email','name','company','role')}
@app.post('/api/logout')
def logout(req:Request,response:Response):
    token=req.cookies.get('jupiter_session')
    if token:
        with db() as c: c.execute('DELETE FROM sessions WHERE token=?',(token,))
    response.delete_cookie('jupiter_session')
    return {'ok':True}
@app.get('/api/me')
def me(req:Request): return current_user(req)
@app.get('/api/config')
def config(req:Request):
    current_user(req)
    return {'tiers':TIERS,'regions':REGIONS,'statuses':STATUSES,'document_labels':DOC_LABELS}
@app.get('/api/deals')
def deals(req:Request,search:str='',status:str='',service:str=''):
    user=current_user(req)
    with db() as c:
        if user['role']=='admin': rows=c.execute('SELECT * FROM deals ORDER BY id DESC').fetchall()
        else: rows=c.execute('SELECT * FROM deals WHERE owner_id=? ORDER BY id DESC',(user['id'],)).fetchall()
    result=[serialize(row) for row in rows]
    if search:
        t=search.casefold(); result=[x for x in result if any(t in str(x['payload'].get(k,'')).casefold() for k in ('model','vin','client')) or t in x['ref'].casefold() or t in x['company'].casefold()]
    if status: result=[x for x in result if x['status']==status]
    if service: result=[x for x in result if service in x['payload'].get('services',[])]
    return result
@app.get('/api/deals/{ident}')
def deal(ident:int,req:Request):
    user=current_user(req)
    with db() as c:
        row=check_deal(c,ident,user)
        d=serialize(row)
        d['attachments']=[dict(x) for x in c.execute('SELECT id,filename,size,created FROM attachments WHERE deal_id=? ORDER BY id DESC',(ident,)).fetchall()]
    return d
@app.post('/api/quotes')
def quote(data:DealIn,req:Request):
    current_user(req)
    return calculate(data.payload)
@app.post('/api/deals',status_code=201)
def create_deal(data:DealIn,req:Request):
    user=current_user(req)
    if data.status not in STATUSES: raise HTTPException(400,'Неверный статус')
    p=data.payload
    if not str(p.get('model','')).strip() or not float(p.get('amount',0) or 0): raise HTTPException(400,'Укажите модель и сумму инвойса')
    if not any(s in ('PAY','CAPITAL','IMPORT') for s in p.get('services',[])): raise HTTPException(400,'Выберите хотя бы одну услугу')
    q=calculate(p)
    timestamp=now()
    with db() as c:
        c.execute('INSERT INTO deals (ref,owner_id,company,created,updated,status,payload,quote,history,notes) VALUES (?,?,?,?,?,?,?,?,?,?)',
                  ('TEMP',user['id'],user['company'],timestamp,timestamp,data.status,json.dumps(p,ensure_ascii=False),json.dumps(q,ensure_ascii=False),json.dumps([{'at':timestamp,'text':'Сделка создана'}],ensure_ascii=False),data.notes))
        ident=c.execute('SELECT last_insert_rowid()').fetchone()[0]
        ref=f'JP-{datetime.now().year%100:02d}-{1000+ident}'
        c.execute('UPDATE deals SET ref=? WHERE id=?',(ref,ident))
    return {'id':ident,'ref':ref,'quote':q}
@app.patch('/api/deals/{ident}')
def update_deal(ident:int,data:DealPatch,req:Request):
    user=current_user(req)
    with db() as c:
        row=check_deal(c,ident,user)
        updates=[]; params=[]
        history=json.loads(row['history'])
        if data.status is not None:
            if data.status not in STATUSES: raise HTTPException(400,'Неверный статус')
            if data.status!=row['status']:
                updates.append('status=?');params.append(data.status)
                history.append({'at':now(),'text':f'Статус изменён на «{data.status}»', 'by':user['name']})
        if data.notes is not None:
            updates.append('notes=?');params.append(data.notes[:10000])
        if data.documents is not None:
            updates.append('documents=?');params.append(json.dumps({k:bool(v) for k,v in data.documents.items() if k in DOC_LABELS},ensure_ascii=False))
            history.append({'at':now(),'text':'Обновлён список документов', 'by':user['name']})
        if updates:
            updates.extend(['history=?','updated=?']);params.extend([json.dumps(history,ensure_ascii=False),now(),ident])
            c.execute('UPDATE deals SET '+','.join(updates)+' WHERE id=?',params)
        return serialize(check_deal(c,ident,user))
@app.get('/api/requests')
def inquiries(req:Request):
    user=current_user(req)
    with db() as c:
        if user['role']=='admin': rows=c.execute('SELECT r.*,u.company FROM requests r JOIN users u ON u.id=r.owner_id ORDER BY r.id DESC').fetchall()
        else: rows=c.execute('SELECT r.*,u.company FROM requests r JOIN users u ON u.id=r.owner_id WHERE r.owner_id=? ORDER BY r.id DESC',(user['id'],)).fetchall()
    return [dict(x) for x in rows]
@app.post('/api/requests',status_code=201)
def inquiry(data:RequestIn,req:Request):
    user=current_user(req)
    with db() as c:
        c.execute('INSERT INTO requests (owner_id,created,type,message) VALUES (?,?,?,?)',(user['id'],now(),data.type,data.message))
        ident=c.execute('SELECT last_insert_rowid()').fetchone()[0]
    return {'id':ident,'status':'Новая'}
@app.get('/api/partners')
def partners(req:Request):
    user=current_user(req)
    if user['role']!='admin': raise HTTPException(403,'Доступно администратору')
    with db() as c:
        return [dict(x) for x in c.execute('SELECT id,name,company,email,role FROM users ORDER BY id')]
@app.post('/api/deals/{ident}/files',status_code=201)
async def upload(ident:int, req:Request, file:UploadFile=File(...)):
    if os.environ.get('JUPITER_PUBLIC_DEMO')=='1':
        raise HTTPException(403,'Загрузка документов отключена в публичном деморежиме')
    user=current_user(req)
    with db() as c: check_deal(c,ident,user)
    allowed={'application/pdf','.pdf','image/jpeg','.jpg','image/png','.png','application/vnd.openxmlformats-officedocument.wordprocessingml.document','.docx'}
    ext=pathlib.Path(file.filename or '').suffix.lower()
    if ext not in {'.pdf','.jpg','.jpeg','.png','.docx'}: raise HTTPException(400,'Допустимы PDF, JPG, PNG, DOCX')
    data=await file.read(8*1024*1024+1)
    if len(data)>8*1024*1024: raise HTTPException(413,'Файл не должен превышать 8 МБ')
    path=UPLOADS/(str(uuid.uuid4())+ext)
    path.write_bytes(data)
    with db() as c:
        c.execute('INSERT INTO attachments (deal_id,filename,path,mime,size,created) VALUES (?,?,?,?,?,?)',(ident,pathlib.Path(file.filename or 'document'+ext).name,str(path),file.content_type or 'application/octet-stream',len(data),now()))
        attachment_id=c.execute('SELECT last_insert_rowid()').fetchone()[0]
    return {'id':attachment_id,'filename':file.filename,'size':len(data)}
@app.get('/api/files/{ident}')
def download(ident:int,req:Request):
    user=current_user(req)
    with db() as c:
        row=c.execute('SELECT * FROM attachments WHERE id=?',(ident,)).fetchone()
        if not row: raise HTTPException(404,'Файл не найден')
        check_deal(c,row['deal_id'],user)
    return FileResponse(row['path'],filename=row['filename'],media_type='application/octet-stream')
@app.get('/api/export.csv')
def export(req:Request):
    user=current_user(req)
    with db() as c:
        rows=c.execute('SELECT * FROM deals ORDER BY id DESC' if user['role']=='admin' else 'SELECT * FROM deals WHERE owner_id=? ORDER BY id DESC', () if user['role']=='admin' else (user['id'],)).fetchall()
    output=io.StringIO();w=csv.writer(output,delimiter=';')
    w.writerow(['Номер','Компания','Модель','Маршрут','Услуги','Статус','Инвойс','Курс','Стоимость в РФ','Создана'])
    for r in rows:
        d=serialize(r);p=d['payload'];q=d['quote']
        w.writerow([d['ref'],d['company'],p.get('model'),p.get('region'),'+'.join(p.get('services',[])),d['status'],p.get('amount'),p.get('fx'),q.get('retail_total'),d['created']])
    stream=io.BytesIO(('\ufeff'+output.getvalue()).encode('utf-8'))
    return StreamingResponse(stream,media_type='text/csv; charset=utf-8',headers={'Content-Disposition':'attachment; filename="jupiter_deals.csv"'})

app.mount('/static',StaticFiles(directory=BASE/'static'),name='static')
@app.get('/')
def index(): return FileResponse(BASE/'static'/'index.html')
@app.get('/landing')
def landing(): return FileResponse(BASE/'static'/'landing.html')

seed()
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=int(os.environ.get('PORT','8000')))
