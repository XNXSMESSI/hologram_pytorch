import argparse
from utils import *
from models.HGN import HGN
from train import train
from test import test
from torchsummary import summary
import torch


def parse_args():
    parser = argparse.ArgumentParser(description="Hologram Generation Net")

    """ Dataset """
    parser.add_argument("--dataset_path", type=str, default="../dataset_rgb")
    parser.add_argument("--use_preTrain", type=int, default=False)

    """ Training Condition """
    parser.add_argument("--is_cuda", type=int, default=True)
    parser.add_argument("--block_num", type=list, default=[2, 2, 2, 2, 2])
    parser.add_argument("--epoch_num", type=int, default=1000)
    parser.add_argument("--batch_size", type=int, default=128)
    parser.add_argument("--learning_rate", type=float, default=0.0001)

    """ Results """
    parser.add_argument("--print_period_error", type=int, default=10)
    parser.add_argument("--print_period_image", type=int, default=10)
    parser.add_argument("--resume", "-r", action="store_true", help="resume from ckpt")

    """ Directories """
    parser.add_argument("--save_image_path", type=str, default="../images")
    parser.add_argument("--save_model_path", type=str, default="../models")

    return check_args(parser.parse_args())


def main():
    """ Hologram Generation Network """

    """ Load Arguments """
    args = parse_args()

    """ GPU check """
    args.is_cuda = torch.cuda.is_available()

    """ Network """
    model = HGN(args.block_num)
    if args.is_cuda:
        model.cuda()

    """ Parameter check """
    summary(model, (3, 64, 64))

    """ Train """
    train(args, model)

    """ Test """
    test(args, model, -1)


if __name__ == "__main__":
    main()