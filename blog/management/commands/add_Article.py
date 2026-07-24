import json

from django.core.management.base import BaseCommand
from blog.models import Articles


class Command(BaseCommand):
    help = "Команда добавления статей"

    def handle(self, *args, **options):
        Articles.objects.all().delete()
        content_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed mollis dolor quis tristique sagittis. Suspendisse aliquet nulla eros, sed maximus enim congue id. Aliquam facilisis lacinia venenatis.
         Sed massa eros, elementum vel neque eget, venenatis vehicula dolor. Nam pharetra purus libero, vitae tincidunt arcu tempus eget. 
         Suspendisse eget nisl vel odio rhoncus mattis. Pellentesque convallis, leo non aliquet fermentum, ante eros eleifend nisl, non sagittis enim nunc et tortor. 
         Aliquam tellus nulla, dictum eget ante sagittis, dignissim facilisis diam.
          Ut sit amet blandit magna. Aenean eu metus nibh. 
         Fusce auctor est libero, quis dictum nisl rhoncus ut. 
         Donec quam lorem, scelerisque vitae ipsum auctor, maximus suscipit felis. 
         Phasellus rutrum ligula ut ipsum ornare, quis aliquet nisi dictum.
Aliquam quis elit dictum, blandit erat nec, mollis neque. 
Aenean tincidunt, ipsum a suscipit facilisis, justo nisi consequat turpis, non mattis ante tellus laoreet purus. 
Nullam tincidunt ligula dolor, in sagittis sem tempus ut. Aenean dictum et arcu quis maximus. 
Suspendisse auctor nulla eu turpis condimentum convallis. Vivamus eu orci pellentesque, rutrum nunc ut, tristique metus. Nam pharetra turpis non mi mattis placerat.
Suspendisse quis consectetur odio. Sed pretium erat non dui consequat, in dictum lectus malesuada. Duis gravida tempus condimentum. 
Vestibulum mollis tellus at felis commodo ultrices. Nulla convallis est mi, interdum sollicitudin tellus auctor eu. 
Donec eget tincidunt dolor. Curabitur hendrerit nibh vel quam congue viverra. Fusce velit nisl, vestibulum et mi sed, maximus dictum mi.
Aliquam condimentum massa non bibendum semper. Sed placerat sapien vitae diam mollis, eu condimentum orci pretium. 
Pellentesque lacinia ut orci faucibus condimentum. Aenean nunc ante, condimentum egestas dui sed, lobortis dignissim nibh. 
Morbi et venenatis purus, sed congue elit. 
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 
Nullam tempor aliquam neque, quis malesuada neque. Morbi tristique nibh eu tortor tincidunt, ac tincidunt massa condimentum. 
Mauris rhoncus tristique tellus, id dignissim lectus.Morbi lacinia ex nec sapien aliquam, vel dictum quam volutpat. 
Aenean non lectus elementum, tempus justo non, scelerisque lacus. Fusce vel tempor nulla, id dapibus mauris. 
Duis id tincidunt tellus, sed rutrum felis. Nam egestas risus id tempus cursus. 
Morbi tincidunt ex vitae scelerisque molestie. Morbi malesuada nec ipsum eu malesuada. 
Aliquam eleifend felis vel tempor vestibulum. Sed consectetur vulputate cursus. 
Phasellus non risus eu elit sodales porttitor. Vivamus tellus justo, dictum a pulvinar sit amet, lacinia eu risus. 
Nunc vel lorem quis lorem varius facilisis. Ut a tortor ipsum.
"""
        for i in range(0,5):

            article1_data = {'title': f'Статья {i}', 'content': content_text,
                             'picture': 'images.png',
                             'is_publicated': True}
            article1, created = Articles.objects.get_or_create(**article1_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {article1.title}'))
