from time import time
from math import log
from json import load, dump
#from htam import prime

__0 = (0).__ne__
__log = log
__int = int
__len = len
__sum = sum
__list = list
__range = range
__tuple = tuple
__filter = filter
__sorted = sorted

def __trunc(x): return x.__trunc__()

def prime2(x):
    try:
        lo = __log(x)
        l = __int(x * (lo + __log(lo)))
        if x > 4100000:
            pl = [2] + [0 if i % 2 == 0 else i for i in __range(3, l)]
            for p in __range(3, __int(l ** (1 / 2)) + 1, 2):
                if pl[p - 2]:
                    for i in __range(p * 2, l, p):
                        pl[i - 2] = 0
            return __tuple(__filter(__0, pl))[x - 1]
        pl = {i for i in __range(3, l, 2)}
        for p in __range(3, x, 2):
            if p in pl:
                for i in __range(p * 2, l, p):
                    pl.discard(i)
        pl = __list(pl)
        pl.sort()
        return pl[x - 2]
    except:
        if x < 1: return None
        elif x == 1: return 2
        elif x == 5: return 11
        else: return 2 * x - 1


#from json import load

def get_highest_stored_prime():
    __c = 0
    try:
        while True:
            with open(f'../htam/primelists/pl{__c}.json') as _: pass
            __c += 1
    except:
        __c -= 1
        with open(f'../htam/primelists/pl{__c}.json') as f:
            l = __load(f)
            return l[-1], __c * __pstep + __len(l)

__ghsp = get_highest_stored_prime

__load = load
__pstep = 100000
with open(f'../htam/primelists/pl0.json') as f: __first_primes = __load(f)
#__first_primes = []

def prime3(x):
    if x < 1: return None
    __gh0, __gh1 = __ghsp()
    if x <= __gh1:
        x -= 1
        with open(f'../htam/primelists/pl{(x // __pstep)}.json') as f: pl = __load(f)
        return pl[x % __pstep]
    lo = __log(x)
    l = __int(x * (lo + __log(lo)))
    pl = [0 if i % 2 == 0 else i for i in __range(l - x, l)]
    for p in __first_primes:
        if p > l ** 0.5 + 1:
            with open('output.json', 'w') as f: dump(__list(__filter(__0, pl)), f, indent = 4); break
            #return __tuple(__filter(__0, pl))
        for i in __range(p * 2, l, p):
            if i > __gh0:
                pl[i - __gh0] = 0
    #with open('output.json') as f: dump(__list(__filter(__0, pl)), f, indent = 4)
    return __tuple(__filter(__0, pl))[x - __gh1]

test = get_highest_stored_prime()[1] + 1

# TEST 1
print('Test 1')
start = time()
print(prime3(test))
end = time()
print(f'Tempo di esecuzione: {end - start}')


'''s1, s2 = 0, 0
for i in range(1000):
    s = time()
    tot(10)
    s1 += time() - s
    s = time()
    tot2(10)
    s2 += time() - s

print(s1)
print(s2)'''

'https://r4---sn-hpa7znsz.googlevideo.com/videoplayback?expire=1616710142&ei=nrVcYLyoN9OegAeR1LMw&ip=93.151.130.25&id=o-ANuwwrsIkrMRWvmcOmXReBB0jfUmtmV2_VLlzPkZxThI&itag=18&source=youtube&requiressl=yes&pcm2=no&gcr=it&vprv=1&mime=video%2Fmp4&ns=B7U_HeXjLOIq5brLRo_37gUF&gir=yes&clen=15929856&ratebypass=yes&dur=212.091&lmt=1578933304205652&fvip=4&fexp=24001373,24007246&c=WEB&txp=5531432&n=YxtR86MkKwcad9y5ejT8t&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&avi=K1A%2FHwERIiwAVF9GR2BFBydLPhE9FxxHSFQmDVNZV0E1FigaFRwsBwECFkYZahBQZkddRVdFIAsGAFIcWV1ZWSEVDxIWFT0KDQMcEFFUEB9yHB0PEB0iFQUFAQJEWVhYPAgRFRMWPwhVRFZUFgcFC2lGSytJVg4MFB4AFndYX1YjBggbFVZ3Rz8qR1UVAAQFaEpZR1wob0k4VFRSEgcHAGlLW045VhAZVUBUUhUJCgZkQUtaRyQhBB0XBw1PWEZKAwYIAhAHb19GOS5GDxNkWjQXBj8LEiIwFhosCkdUShFqQkVUPCAuChEYERZaEwgRGSZLWkckPwocD0deAVlGRyBIRlkMAGAVFlgKHFpdU1EjXAAZX0Z%2FUFJFR0gBfFNLHRsHEiYbOAsQBBxGGRN7Z3JeSzUQBj8ACgIxDU5UQUcxHxlUX1Z8U1VAU1wbBAYAcl5LMx0APwQHAgoWd0hCVnJISxwWGyMsCiYEA0YTTw%3D%3D&sig=AOq0QJ8wRQIhAKnyi75okZVNfNMk-qZOSmZXpV71UMXPgdc9VbxAkPlBAiBK_Nk2rSUiweB-CNiAzyfD0OrJx3MwGZP4TEqEmwriNA%3D%3D&from_cache=False&title=Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up%20(Video)&rm=sn-8vq54voxpu-ca9e7z,sn-hpazk7z&req_id=dcae6260dd59a3ee&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mh=7c&mip=87.7.238.165&mm=29&mn=sn-hpa7znsz&ms=rdu&mt=1616688149&mv=u&mvi=4&pl=24&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgS_jtd_KnQzINZ3kyG6hE8eo0U9E8_5NoymtkXI7i2mICIHio4fq2v4FuJKjdy7u2pu5b-gMOrp6kLiMozCPsixOS'