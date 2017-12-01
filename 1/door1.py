INPUT = '9514845965411415573169847814949991796797677476271324475131716264245617796628731577614429522' \
        '1229668557345231126344516323349319921138783846159463566669942298294778262331733368397843812' \
        '3261326863959719777179228599319321138948466562743761584836184512984131635354116264899181952' \
        '7482245239539764858162952279457925557261219133449594544588294854711744157752788653241427333' \
        '3978987892959627599834177887388958581991645747477325224917936659995145418265722557627783466' \
        '9222982366884688565754691273745959468648957498511326215934353963981471593984617554514519623' \
        '7853268883747421473189934232148347517859569583951334866563884545527697225625244157159138699' \
        '4632555139663859339872993852642499434826793515355585155228722331338358366991294136434469472' \
        '5478258297498969517632881187394141593479818536194597976519254215932257653777455227477617957' \
        '8332734632165936423942152753147349147197266189231779183426643519542526672532338588143653517' \
        '2293871662154422659895625775321224885925835136317478274233696142532538156157599235241551416' \
        '8782816173861148859478285339529151631429536819286498721812323861771638574344416879476255929' \
        '9291579129841517426132687547796853961259545953181349333666265944982499563887717237772427726' \
        '5467844881584455537289257474773567236829982654825474435937766729476455933465952323314658756' \
        '8261116253155189394188696831691284711264872914348961888253386971994431352474717376878745948' \
        '7691712432426212199123787317555443872494439973823997147383518577523293679976651669564675444' \
        '5981758291547851448654145393217559841355425967211736486311259251598892274716484266836192513' \
        '5551248923449968328385889877512156952725198691746951431443497496455761516486573476185321748' \
        '5236442834941811193998743246839223935476828519314359312762677667727982615631179546485764217' \
        '4138482349418789527258257566968527998698835779613879432612585277299544635572321116152316188' \
        '6222562853546488411563473998633847953246787557146187696947831335722888918172961256498971868' \
        '9462372995234748419835273914899623571964339272517987643624939658949955926832966518747873842' \
        '4732664388677496682865739371762659157832117483222243412881787176534727815279942556563352115' \
        '2643686221411129463425496425385516719682884157452772141585743166647191938727971366274357874' \
        '252166721759'


def solve(puzzle):
    return sum([int(z) for i, z in enumerate(puzzle) if z == (puzzle[i+1] if i+1 < len(puzzle) else puzzle[0])])


if __name__ == '__main__':
    captcha = solve(INPUT)
    print(captcha)

