#!/usr/bin/env python3
"""
Author : Moshe Steyn and Travis Simmons
Date   : today
Purpose: Rock the Casbah
"""
# Sample deployment

# python3 prepare.py -i /home/u24/travissimmons/cjx/season10/50_hand_label_test_2020_03_02 -o /home/u24/travissimmons/cjx/season10/gifs
# makeflow process.makeflow -j 1

import argparse
import os
import shutil
import sys
import glob
import subprocess





# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--indir',
                        help='Input directory containing pointclouds',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory for gifs',
                        metavar='str',
                        type=str,
                        default='')



    return parser.parse_args()

def main():
    """Make a jazz noise here"""


    if os.path.exists('./process.makeflow'):
        os.remove('./process.makeflow')
    
    shutil.copy('./empty.makeflow', './process.makeflow')


    args = get_args()
    dirs = glob.glob(os.path.join(args.indir, '*'))
    print(dirs)
    files = [os.path.join(i, 'combined_multiway_registered.ply') for i in dirs]
    print(files)

    print(f'Preparing to process {len(files)} files.')


    subprocess.run(['singularity', 'build', '3d_gif_generation.simg', 'docker://phytooracle/3d_segmentation_gif_generation'])

    my_file = open("process.makeflow", "w")
    for i in files:
        if os.path.exists(i):
            pcd_path = i
            output_dir = args.outdir
            array_path = pcd_path.replace('.ply', '.npy')
            plant_name = pcd_path.split('/')[-2]
            gif_path = os.path.join(output_dir, plant_name + '.gif')



            procesing_format = [gif_path + ' ', ':', ' 3d_gif_generation.simg ', array_path + ' ', pcd_path, '\n\t', f'singularity run 3d_gif_generation.simg -i {pcd_path} -o {output_dir}\n\n']

            my_file.writelines(procesing_format)

        else:
            print(i)

    my_file.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
