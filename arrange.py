from PIL import Image
import os
import argparse

def arrange_files(args):
    host_dir = args.host_dir
    target_dir = args.target_dir
    classes = os.listdir(host_dir)
    for class_name in classes:
        if not os.path.exists(os.path.join(target_dir, class_name)):
            os.makedirs(os.path.join(target_dir, class_name))
        instances = os.listdir(os.path.join(host_dir, class_name))
        for instance_name in instances:
            image = Image.open(os.path.join(host_dir, class_name, instance_name, 'rendering/00.png'))
            image_resized = image.resize((256, 256))
            image_resized.save(os.path.join(target_dir, class_name, f'{class_name}_{instance_name}.png'))
        print(f'--------{class_name} Arranged--------')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--host_dir', default='shapenet-images/ShapeNetRendering')
    parser.add_argument('--target_dir', default='shapenet_images/')
    args = parser.parse_args()
    arrange_files(args)

if __name__ == '__main__':
    main()