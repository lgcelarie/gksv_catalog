INSERT INTO `gksvcat_dev_db`.`categorias` (`nombre`, `slug`, `peq_desc`, `imagen`, `estado`) VALUES ('Figuras', 'figuras', 'figuras para todos los gustos. Funko, Furyu, y muchos mas', '1_3.jpg', 'ACTIVO');
INSERT INTO `gksvcat_dev_db`.`categorias` (`nombre`, `slug`, `peq_desc`, `imagen`, `estado`) VALUES ('Pines', 'pines', 'Pines para adornar tu mochila o chaqueta. Marca funko o lootcrate', '1_3.jpg', 'ACTIVO');
INSERT INTO `gksvcat_dev_db`.`categorias` (`nombre`, `slug`, `peq_desc`, `imagen`, `estado`) VALUES ('Llaveros', 'llaveros', 'Llaveros para todos los gustos. Marcas como Funko, bioworld y otras', '1_3.jpg', 'ACTIVO');
INSERT INTO `gksvcat_dev_db`.`categorias` (`nombre`, `slug`, `peq_desc`, `imagen`, `estado`) VALUES ('Lanyards', 'lanyards', 'Lanyards para mostrar tu estilo, en marcas como Funko y Bioworld', '1_3.jpg', 'ACTIVO');
INSERT INTO `gksvcat_dev_db`.`categorias` (`nombre`, `slug`, `peq_desc`, `imagen`, `estado`) VALUES ('Accesorios', 'accesorios', 'Lleva parte de tu juego o serie contigo al vestir. Aritos, dijes o parches', '1_3.jpg', 'ACTIVO');


INSERT INTO `gksvcat_dev_db`.`marcas` (`id`,`nombre`,`imagen`,`slug`) VALUES (1,'Funko','1_1.jpg','funko');
INSERT INTO `gksvcat_dev_db`.`marcas` (`id`,`nombre`,`imagen`,`slug`) VALUES (2,'Bioworld','1_1.jpg','bioworld');
INSERT INTO `gksvcat_dev_db`.`marcas` (`id`,`nombre`,`imagen`,`slug`) VALUES (3,'Furyu','1_1.jpg','furyu');
INSERT INTO `gksvcat_dev_db`.`marcas` (`id`,`nombre`,`imagen`,`slug`) VALUES (4,'Lootcrate','1_1.jpg','lootcrate');


INSERT INTO `gksvcat_dev_db`.`productos` (`id`,`nombre`,`estado`,`cant_visto`,`peq_desc`,`descripcion`,`marca_id`,`condicion`,`slug`) VALUES (1,'Funko Pop Movies: Batman v Superman Batman','DISPONIBLE',0,'bacman','super funko pop de bakmaaaaan',1,9.5,'funko-pop-batman-v-superman-batman');
INSERT INTO `gksvcat_dev_db`.`productos` (`id`,`nombre`,`estado`,`cant_visto`,`peq_desc`,`descripcion`,`marca_id`,`condicion`,`slug`) VALUES (2,'Producto 2','RESERVADO',0,'producto2','osdsdfapjfdsajidsfaijfsdaidsdsaidjfasdfasdfdapjdfadsf',2,7.2,'producto2');


INSERT INTO `gksvcat_dev_db`.`imagenes` (`id`,`primaria`,`ruta`,`producto_id`) VALUES (1,1,'1_1.jpg',1);
INSERT INTO `gksvcat_dev_db`.`imagenes` (`id`,`primaria`,`ruta`,`producto_id`) VALUES (2,0,'1_2.jpg',1);
INSERT INTO `gksvcat_dev_db`.`imagenes` (`id`,`primaria`,`ruta`,`producto_id`) VALUES (3,0,'1_3.jpg',1);


INSERT INTO `gksvcat_dev_db`.`productos_x_categoria` (`producto_id`, `categoria_id`) VALUES ('1', '1');
INSERT INTO `gksvcat_dev_db`.`productos_x_categoria` (`producto_id`, `categoria_id`) VALUES ('2', '2');
