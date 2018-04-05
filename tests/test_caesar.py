#!/usr/bin/env python2

import unittest

try:
    from classical_cipher.caesar import CaesarCipher
except ImportError:
    import sys
    import os
    sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
    from classical_cipher.caesar import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_encode(self):
        # testcases: each is a tuple (a, k, b) where CaesarCipher.encode(a, k) = b
        testcases = [
            (
                "Twilio",
                1,
                "Uxjmjp"
            ),
            (
                "The quick brown fox jumps over the lazy dog.",
                7,
                "Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn."
            ),
            (
                "The quick brown fox jumps over the lazy dog.",
                26,
                "The quick brown fox jumps over the lazy dog."
            ),
            # greater than alphabet length
            (
                "The quick brown fox jumps over the lazy dog.",
                28,
                "Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi."
            ),
            # very large key
            (
                "The quick brown fox jumps over the lazy dog.",
                10008,
                "Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme."
            ),
        ]

        for a, k, solution in testcases:
            result = CaesarCipher.encode(a, k)
            self.assertEqual(result, solution)

    def test_entropy_analysics(self):
        # testcases: each is a tuple (msg, e) where e = CaesarCipher.entropy_analysics(msg)
        testcases = [
            ('Accepts messages', 62.594804275),
            ("That's the never ending story of Robert.", 128.908800926),
        ]
        for msg, e in testcases:
            result = CaesarCipher.entropy_analysics(msg)
            self.assertAlmostEqual(result, e)

    def test_crack(self):
        plaintexts = [
            "London calling to the faraway towns",
            "Now war is declared and battle come down",
            "London calling to the underworld",
            "Come out of the cupboard, you boys and girls",
            "London calling, now don't look to us",
            "Phony Beatlemania has bitten the dust",
            "London calling, see we ain't got no swing",
            "'Cept for the ring of that truncheon thing",
            "The ice age is coming, the sun is zooming in",
            "Meltdown expected, the wheat is growin' thin",
            "Engines stop running, but I have no fear",
            "Cause London is drowning, and I, I live by the river",
            "London calling to the imitation zone",
            "Forget it, brother, you can go it alone",
            "London calling to the zombies of death",
            "Quit holding out and draw another breath",
            "London calling and I don't want to shout",
            "But when we were talking I saw you nodding out",
            "London calling, see we ain't got no high",
            "Except for that one with the yellowy eye",
            "Now get this",
            "London calling, yes, I was there, too",
            "An' you know what they said? Well, some of it was true!",
            "London calling at the top of the dial",
            "And after all this, won't you give me a smile?",
            "I never felt so much a' like a'like a'like",
            "When they kick at your front door",
            "How you gonna come?",
            "With your hands on your head",
            "Or on the trigger of your gun",
            "When the law break in",
            "How you gonna go?",
            "Shot down on the pavement",
            "Or waiting on death row",
            "You can crush us",
            "You can bruise us",
            "But you'll have to answer to",
            "Oh, the guns of Brixton",
            "The money feels good",
            "And your life you like it well",
            "But surely your time will come",
            "As in heaven, as in hell",
            "You see, he feels like Ivan",
            "Born under the Brixton sun",
            "His game is called survivin'",
            "At the end of the harder they come",
            "You know it means no mercy",
            "They caught him with a gun",
            "No need for the Black Maria",
            "Goodbye to the Brixton sun",
            "You can crush us",
            "You can bruise us",
            "Yes, even shoot us",
            "But oh-the guns of Brixton",
            "Shot down on the pavement",
            "Waiting in death row",
            "His game is called survivin'",
            "As in heaven as in hell",
            "Anybody who makes speeches written ",
            "by someone else is just a robot."]

        ciphertexts = [
            "Cfeufe trcczex kf kyv wrirnrp kfnej",
            "Tuc cgx oy jkirgxkj gtj hgzzrk iusk juct",
            "Twvlwv kittqvo bw bpm cvlmzewztl",
            "Lxvn xdc xo cqn ldykxjam, hxd kxhb jwm praub",
            "Bedted sqbbydw, dem ted'j beea je ki",
            "Yqxwh Knjcunvjwrj qjb krccnw cqn mdbc",
            "Hkjzkj ywhhejc, oaa sa wej'p ckp jk osejc",
            "'Lnyc oxa cqn arwp xo cqjc cadwlqnxw cqrwp",
            "Lzw auw syw ak ugeafy, lzw kmf ak rggeafy af",
            "Rjqyitbs jcujhyji, ymj bmjfy nx lwtbns' ymns",
            "Oxqsxoc cdyz bexxsxq, led S rkfo xy pokb",
            "Usmkw Dgfvgf ak vjgofafy, sfv A, A danw tq lzw janwj",
            "Cfeufe trcczex kf kyv zdzkrkzfe qfev",
            "Oxapnc rc, kaxcqna, hxd ljw px rc juxwn",
            "Twvlwv kittqvo bw bpm hwujqma wn lmibp",
            "Mqep dkhzejc kqp wjz znws wjkpdan xnawpd",
            "Gjiyji xvggdib viy D yji'o rvio oj ncjpo",
            "Mfe hspy hp hpcp elwvtyr T dlh jzf yzootyr zfe",
            "Jmlbml ayjjgle, qcc uc ygl'r emr lm fgef",
            "Votvgk wfi kyrk fev nzky kyv pvccfnp vpv",
            "Stb ljy ymnx",
            "Ehgwhg vteebgz, rxl, B ptl maxkx, mhh",
            "Iv' gwc svwe epib bpmg aiql? Emtt, awum wn qb eia bzcm!",
            "Svukvu jhsspun ha aol avw vm aol kphs",
            "Reu rwkvi rcc kyzj, nfe'k pfl xzmv dv r jdzcv?",
            "E jaran bahp ok iqyd w' hega w'hega w'hega",
            "Lwtc iwtn zxrz pi ndjg ugdci sddg",
            "Yfn pfl xfeer tfdv?",
            "Lxiw ndjg wpcsh dc ndjg wtps",
            "Il ih nby nlcaayl iz siol aoh",
            "Bmjs ymj qfb gwjfp ns",
            "Mtb dtz ltssf lt?",
            "Hwdi sdlc dc iwt epktbtci",
            "Tw bfnynsl ts ijfym wtb",
            "Qgm usf ujmkz mk",
            "Gwc kiv jzcqam ca",
            "Jcb gwc'tt pidm bw ivaemz bw",
            "Mf, rfc eslq md Zpgvrml",
            "Kyv dfevp wvvcj xffu",
            "Wjz ukqn heba ukq hega ep sahh",
            "Rkj ikhubo oekh jycu mybb secu",
            "Xp fk ebxsbk, xp fk ebii",
            "Hxd bnn, qn onnub urtn Rejw",
            "Uhkg ngwxk max Ukbqmhg lng",
            "Opz nhtl pz jhsslk zbycpcpu'",
            "Fy ymj jsi tk ymj mfwijw ymjd htrj",
            "Fvb ruvd pa tlhuz uv tlyjf",
            "Znke igamnz nos cozn g mat",
            "Yz yppo qzc esp Mwlnv Xlctl",
            "Zhhwurx mh max Ukbqmhg lng",
            "Vlr zxk zorpe rp",
            "Oek sqd rhkyiu ki",
            "Lrf, rira fubbg hf",
            "Kdc xq-cqn pdwb xo Kargcxw",
            "Dsze ozhy zy esp algpxpye",
            "Osalafy af vwslz jgo",
            "Efp dxjb fp zxiiba prosfsfk'",
            "Rj ze yvrmve rj ze yvcc",
            "Ylwzmbw ufm kyicq qnccafcq upgrrcl ",
            "ur lhfxhgx xelx bl cnlm t khuhm."]

        for plaintext, ciphertext in zip(plaintexts, ciphertexts):
            cache = {}
            key, msg = CaesarCipher.crack(ciphertext, cache)
            self.assertEqual(msg, plaintext)


if __name__ == '__main__':
    unittest.main()

