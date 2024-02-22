from scapy.all import *
from time import *

# covert info to be transmitted
covert_info = "This is covert info"

normal_data = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus viverra fringilla eros sit amet tempor. Aenean vestibulum in sem ac efficitur. Integer luctus ante vel molestie lobortis. Nullam ac aliquet elit. Integer eu lacinia felis. Donec vitae nisl vestibulum, posuere justo a, congue tortor. Aliquam erat volutpat. Aenean quis ex rhoncus, dapibus mauris eu, convallis tellus. Suspendisse semper elit vel dolor ullamcorper bibendum.

Morbi faucibus eget metus sed laoreet. Cras accumsan commodo cursus. Donec vel malesuada diam. Praesent tempus tellus vitae diam tincidunt egestas quis id neque. Ut sed fermentum justo, vel tincidunt odio. Integer nec massa vel magna rutrum aliquet ut quis leo. In in fermentum purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet finibus massa, vel scelerisque elit. Curabitur sit amet velit nec nunc efficitur dapibus et in orci. Vestibulum lorem urna, interdum ac ante in, dignissim sodales magna. Ut sodales libero id purus faucibus fermentum.

Praesent iaculis, orci non efficitur finibus, odio dui lobortis tellus, efficitur accumsan ipsum magna eget orci. Ut mauris leo, sollicitudin quis mi ac, egestas imperdiet lectus. Phasellus in neque nisl. Nullam semper velit ut enim lacinia, quis imperdiet orci hendrerit. Praesent sed nunc mollis, volutpat dolor id, faucibus nulla. Praesent ac justo libero. Fusce pulvinar, metus et gravida euismod, velit mi dictum diam, id scelerisque neque arcu sit amet lacus. Praesent ac feugiat turpis. Nulla rhoncus neque eget est egestas tincidunt. Proin fringilla lacinia cursus. Morbi semper convallis luctus.

Sed eleifend purus id dictum dapibus. Fusce eget enim lectus. Donec eleifend euismod blandit. Fusce maximus elementum lorem, sit amet gravida lacus porta dapibus. Sed laoreet ante non lorem bibendum imperdiet. Etiam dapibus orci a dictum lacinia. Morbi vitae sem vel nisi lobortis semper. Maecenas a tortor risus. In sit amet porttitor felis, nec ultrices diam. Vestibulum commodo ullamcorper tellus quis posuere. Integer eleifend aliquet tristique. Curabitur sit amet pulvinar elit. Nam semper mi vitae semper ultrices. Nulla in eros sit amet diam eleifend fringilla tincidunt vestibulum est.

Vivamus magna justo, pharetra eget dui id, porta laoreet diam. Aliquam sapien nisi, commodo ultrices erat at, vestibulum consectetur risus. Nullam at porta nisi, sed faucibus dui. Curabitur pretium eget elit vitae laoreet. Nulla mollis sollicitudin dolor, vitae rutrum metus sodales non. Morbi vel consectetur dui. Vivamus eleifend sed sem at porttitor. Curabitur sit amet leo nunc. Nulla facilisi. Phasellus fermentum ultricies magna, a convallis felis sollicitudin non. Sed at leo consectetur turpis ultricies porttitor. Morbi imperdiet eros feugiat metus tristique rhoncus.

Sed vitae elit dolor. Aenean et sem ac ex semper congue nec vel dui. Integer suscipit in ligula eu vulputate. Donec rutrum eros sit amet erat gravida, et ornare justo pulvinar. Sed ultricies lacinia orci, at consectetur lacus pretium et. Phasellus vestibulum odio volutpat efficitur suscipit. Fusce consequat quam nec ipsum feugiat vulputate. Phasellus ac ex ut augue sagittis pretium. Etiam in mi at elit sagittis interdum. Duis quis ligula eget quam laoreet dapibus ut at lacus. Donec non tempus elit. In hac habitasse platea dictumst. Nam sit amet urna nec diam pharetra luctus. Aliquam commodo auctor rutrum. Cras dignissim sodales congue.

Duis vitae velit et turpis euismod porta et a massa. Nunc sem elit, maximus id nibh eu, efficitur rutrum ex. Proin quis orci mauris. Fusce euismod arcu eget hendrerit luctus. Pellentesque cursus, arcu sit amet vulputate laoreet, tortor orci facilisis ex, non fringilla lorem metus accumsan augue. Suspendisse sed interdum mauris. Suspendisse ac fermentum quam, eu egestas lorem.

Maecenas non consectetur dolor. Pellentesque ultricies libero non est auctor, at sodales orci sagittis. Proin elementum auctor massa at convallis. Donec mauris libero, porttitor vitae neque gravida, imperdiet accumsan enim. Mauris purus urna, placerat vel turpis ac, dapibus volutpat ex. Phasellus sed ipsum in metus pellentesque posuere vel a sem. Pellentesque maximus venenatis risus, vitae vestibulum diam finibus sit amet. Phasellus scelerisque pretium dui, sed consequat ipsum finibus id. Vestibulum non iaculis ex. In vitae massa vitae mauris venenatis laoreet at vel magna. Aenean fermentum tellus ut erat sollicitudin tempor.

In viverra dolor in eleifend facilisis. Sed lobortis eros eu finibus feugiat. In hendrerit diam eu dui vestibulum posuere. Praesent ultrices blandit condimentum. Morbi in iaculis nisi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam nec facilisis augue. Pellentesque maximus quis tortor non luctus. Proin a mauris urna.

Quisque nisi elit, auctor sit amet laoreet id, rhoncus ut leo. Donec non efficitur nisi. Pellentesque malesuada facilisis feugiat. Integer tempor dui sit amet gravida varius. Cras vel diam ac nisl tempor blandit a et ex. Suspendisse ullamcorper nisl non vestibulum imperdiet. Ut dictum, sapien id maximus pharetra, velit velit pellentesque eros, quis pharetra purus lectus at magna. Vestibulum semper ipsum et velit faucibus egestas. Aenean pulvinar purus mi, ut ultricies tellus euismod vel. Proin quis auctor leo, sit amet ornare velit. Sed sit amet semper eros, ut fermentum neque. Etiam maximus malesuada efficitur. Sed fringilla consectetur dui, et consequat sapien finibus et. Suspendisse tristique neque arcu, et feugiat odio consectetur ac. Duis pulvinar, ex vel sodales malesuada, tortor leo ultricies nunc, id pellentesque nibh enim sed felis.

Maecenas aliquam venenatis tortor ut placerat. Aenean molestie id diam in congue. Morbi euismod urna efficitur elit vestibulum congue. Donec pharetra et lacus non tristique. Praesent venenatis vehicula erat, vel suscipit purus accumsan sed. Suspendisse pulvinar, dolor quis auctor facilisis, ligula leo lacinia leo, sit amet scelerisque tortor leo quis nibh. Suspendisse vel justo ipsum. In scelerisque in est in varius. Etiam ac lacus a leo viverra pretium. Donec lectus velit, pulvinar eu nibh in, dapibus dictum metus. Nunc mollis libero sit amet efficitur sodales. Praesent vestibulum, risus vitae molestie vestibulum, est nibh pharetra risus, quis eleifend metus libero a felis. Donec ultricies tellus ut magna pretium, feugiat porttitor sapien interdum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent id nisl in eros pretium dapibus a eget lorem. Suspendisse vehicula congue mauris et eleifend.

In et semper est. Etiam laoreet nec lacus nec aliquet. Maecenas et suscipit erat, in imperdiet magna. Nulla ac tellus vehicula, finibus justo sed, egestas nisl. Nunc ultrices urna ligula, et vulputate enim tempus pretium. Donec blandit, leo ut pharetra eleifend, libero justo gravida massa, sed molestie libero odio quis enim. Nullam congue sit amet sapien sed blandit.

Sed eu massa vitae erat hendrerit tempus. Cras sit amet nibh odio. Proin in nulla a libero commodo semper. Donec ultrices nisi ligula, sit amet aliquet dolor feugiat in. Nulla dapibus congue orci a luctus. Cras vestibulum lacus ut gravida pellentesque. Duis ullamcorper dolor id tellus posuere viverra. Proin hendrerit nibh ac aliquet sodales. Aenean laoreet faucibus arcu, a pharetra justo efficitur varius. Aliquam erat volutpat. Mauris eget augue blandit, feugiat nibh eget, aliquet tortor. Vestibulum dignissim nisi sit amet nisl efficitur facilisis. Curabitur lobortis magna enim. Curabitur consequat pulvinar diam, nec porttitor quam maximus vel. Vestibulum rutrum sollicitudin sagittis.

Donec id enim eu lectus accumsan scelerisque non quis dolor. Donec a congue massa. Vivamus pharetra fermentum orci sit amet aliquam. Phasellus vitae velit erat. Nulla facilisi. Vivamus eget feugiat eros, et ornare neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc feugiat sollicitudin cursus. In rutrum ipsum a sem bibendum aliquam. Integer bibendum, est ac laoreet varius, lacus dui ultrices libero, ac rutrum quam diam vitae eros. Ut ac euismod nulla.

Aenean sem lorem, tristique at vestibulum ac, rutrum et elit. Nulla semper, ex a pulvinar tempor, nulla nisl tempor ipsum, id sagittis libero quam non lorem. Vestibulum varius ante nulla, a gravida enim molestie ac. Sed pretium vestibulum ipsum non mollis. Morbi et tortor eget velit viverra dignissim. Integer sollicitudin, erat porttitor malesuada viverra, lectus ipsum tempor quam, vel commodo dui turpis et nisl. Nullam commodo laoreet lacus vel elementum. Mauris et leo libero. Ut rutrum metus non est egestas, ultricies scelerisque est bibendum. Nunc vitae metus sollicitudin, rutrum augue sit amet, volutpat nibh. Fusce id fringilla ipsum. Proin aliquet diam at nulla suscipit condimentum. Aenean volutpat, dui id semper mollis, sapien diam condimentum purus, nec malesuada augue risus a leo. Sed orci justo, molestie et nisl vitae, eleifend lobortis augue.

Nulla posuere laoreet purus, non varius odio venenatis ut. Quisque eu libero erat. Cras placerat ut nunc eget posuere. Nullam ligula arcu, auctor pharetra euismod quis, tempus sed leo. Mauris quis orci sed mi suscipit ornare. Mauris mattis consectetur mi, non luctus est laoreet id. Aenean sit amet ex sodales, luctus neque ac, vestibulum sem. Sed in diam ac odio finibus mattis eu elementum sapien. Aliquam erat volutpat.

Vivamus porttitor, nibh et ornare consectetur, lorem nibh finibus urna, eget mollis est ex in elit. Cras aliquet feugiat lacinia. Cras dui erat, facilisis ut blandit ultricies, fringilla pharetra arcu. Suspendisse aliquam interdum auctor. Duis urna mi, tincidunt eget nisl sed, hendrerit viverra felis. Morbi ex felis, tristique nec mauris ut, ullamcorper convallis dui. Proin sodales leo pretium sem semper, vitae tempor mauris condimentum. Curabitur sed diam ac purus tristique bibendum. Fusce blandit auctor libero, porttitor sodales ligula vestibulum vitae. Sed consequat gravida sagittis. Donec placerat, lectus id hendrerit volutpat, ante risus hendrerit dui, eget accumsan tortor neque ut orci.

Sed nec ligula sed enim tempor rhoncus eu et nisl. Donec faucibus orci vitae tellus posuere, elementum posuere nibh dictum. Mauris quis tellus tortor. Interdum et malesuada fames ac ante ipsum primis in faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin laoreet a nunc vel gravida. Donec in quam fringilla, blandit leo non, viverra ex. Nulla commodo dui lacus, consectetur auctor neque euismod eget. Donec finibus, ante nec aliquam bibendum, sapien purus maximus enim, id mattis arcu felis quis nisi. Duis non elit ac metus posuere eleifend nec at est. Suspendisse sagittis turpis nec orci suscipit, consectetur tincidunt mauris pellentesque. Nunc interdum dictum justo vitae viverra. Vivamus ultrices cursus nisi a placerat. Etiam sed dui gravida, hendrerit mi eu, scelerisque mi. Donec aliquet eget nibh ac pellentesque. Aenean interdum leo pretium est tincidunt dapibus.

Vivamus ex lorem, dictum nec consequat a, blandit sed quam. Proin pulvinar dolor nec lacus tincidunt aliquet. Aenean a nisl volutpat, dignissim mi vel, convallis magna. Duis pellentesque lobortis nulla, vel ultrices purus venenatis sit amet. Mauris elementum lacinia felis, blandit ultricies arcu tempor iaculis. Aenean vestibulum consequat justo at fringilla. Vivamus ultricies urna risus, condimentum tincidunt mauris ornare eu. Duis faucibus porttitor orci, et efficitur orci sollicitudin a. Suspendisse potenti. Maecenas egestas, urna sed sagittis aliquam, enim sem tempus mi, eget gravida mi ligula non nisi.

Sed luctus leo et libero sollicitudin volutpat. Proin ut tortor tellus. Phasellus bibendum lorem lacus, a auctor turpis feugiat ac. Cras a erat lectus. Curabitur pulvinar, nisi in tempus sodales, ante tellus pulvinar eros, euismod finibus dui velit at ipsum. Mauris pharetra sit amet orci at sollicitudin. Maecenas scelerisque sem sit amet velit suscipit, et viverra nulla lacinia. Donec dignissim erat vel libero congue venenatis.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce non est vel neque lacinia auctor et sed purus. Aliquam mollis neque ex, eu fringilla tortor posuere sed. Cras sodales neque eget nibh pretium consectetur. Duis pretium ex eu eros aliquam, ac rhoncus felis imperdiet. Curabitur rutrum egestas diam vitae condimentum. Vestibulum commodo, ipsum id suscipit tincidunt, leo velit finibus tellus, a lacinia lacus tortor in massa. Mauris volutpat tortor in libero consequat lacinia. Vivamus velit dui, varius non cursus vitae, sagittis eu lectus. Praesent luctus porttitor venenatis. Proin ut rhoncus diam, nec rhoncus nisl. Nam mattis sagittis consequat. Nam vitae sollicitudin nibh. Cras eget maximus ante, mattis scelerisque lorem. Nullam ac sagittis magna.

Fusce eget eros lorem. Nam enim urna, luctus quis commodo vitae, elementum in urna. Aenean tempor faucibus ultricies. Aliquam tortor eros, tempor vel vulputate sit amet, ultrices sed nisi. Fusce semper ligula in varius blandit. Pellentesque scelerisque interdum sem nec ullamcorper. Aliquam suscipit ac lacus quis sodales. Phasellus vel dolor condimentum est condimentum viverra. Aenean condimentum libero mi, ut mattis sapien tristique quis. Mauris eleifend arcu sit amet mi cursus, rhoncus rutrum quam volutpat.

"""
data = list(normal_data)

# convert covert info to bit stream
covert_bits = [int(b) for b in ''.join(format(ord(c), '08b') for c in covert_info)]
covert_bits.insert(0,0)
print(covert_bits)

# function to modify timing information in TCP packet
def modify_timing(pkt, bit):
    # set last bit of time field to bit value
    if bit:
        sleep(1)
    send(pkt)

# function to send TCP packet with covert bit
def send_packet(covert_bit,data,c):
    # create TCP packet with payload of normal data
    #Sending 1000 bytes of data
    send_data = "".join(data[c:c+1000])
    pkt = IP(dst="10.0.2.7")/UDP(dport=8080)/send_data
    # modify timing information with covert bit
    modify_timing(pkt, covert_bit)
    c += 1
    return c


# loop through covert bit stream and send packets
c = 0
for bit in covert_bits:
	c = send_packet(bit,data,c)