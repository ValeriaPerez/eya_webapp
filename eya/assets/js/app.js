import base from './base/base';
import header from './base/header';
import menu from './base/menu';

import popupDetail from './products/popup_detail';
import productCarousel from './owl-carousel/products-carousel';

import toggle from './users/toggle';

import owl from './plugins/owl.carousel.min.js';

base();
header();
menu();

productCarousel();
popupDetail();

toggle();

owl();